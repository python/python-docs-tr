import os
import re
import sys
from argparse import ArgumentParser
from typing import Dict, Tuple

import polib
from deep_translator import DeeplTranslator, GoogleTranslator

parser = ArgumentParser()
parser.add_argument("filename", help="File to translate")
parser.add_argument(
    "-t",
    "--translator",
    choices=["google", "deepl"],
    default="deepl",
    help="Translator to use",
)
parser.add_argument(
    "-a",
    "--api-key",
    required="deepl" in list(map(lambda x: x.casefold(), sys.argv)),
    help="API key for DeepL (required if using DeepL)",
)
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
parser.add_argument("-d", "--debug", action="store_true", help="Debug mode")
parser.add_argument(
    "-s",
    "--skip-translated-entries",
    choices=[True, False],
    default=True,
    help="Skip already translated entries",
)

args = parser.parse_args()

VERBOSE = args.verbose
DEBUG = args.debug
SKIP_TRANSLATED_ENTRIES = args.skip_translated_entries


_patterns = [
    ":c:func:`[^`]+`",
    ":c:type:`[^`]+`",
    ":c:macro:`[^`]+`",
    ":c:member:`[^`]+`",
    ":c:data:`[^`]+`",
    ":py:data:`[^`]+`",
    ":py:mod:`[^`]+`",
    ":func:`[^`]+`",
    ":mod:`[^`]+`",
    ":ref:`[^`]+`",
    ":class:`[^`]+`",
    ":pep:`[^`]+`",
    ":data:`[^`]+`",
    ":exc:`[^`]+`",
    ":term:`[^`]+`",
    ":meth:`[^`]+`",
    ":envvar:`[^`]+`",
    ":file:`[^`]+`",
    ":attr:`[^`]+`",
    ":const:`[^`]+`",
    ":issue:`[^`]+`",
    ":opcode:`[^`]+`",
    ":option:`[^`]+`",
    ":program:`[^`]+`",
    ":keyword:`[^`]+`",
    ":RFC:`[^`]+`",
    ":rfc:`[^`]+`",
    ":doc:`[^`]+`",
    ":source:`[^`]+`",
    ":manpage:`[^`]+`",
    ":mimetype:`[^`]+`",
    ":sup:`[^`]+`",
    ":kbd:`[^`]+`",
    ":const:`[^`]+`",
    "``[^`]+``",
    "`[^`]+`__",
    "`[^`]+`_",
    r"\*\*[^\*]+\*\*",  # bold text between **
    r"\*[^\*]+\*",  # italic text between *
]

_exps = [re.compile(e) for e in _patterns]


def protect_sphinx_directives(s: str) -> Tuple[dict, str]:
    """
    Parameters:
        string containing the text to translate
    Returns:
        dictionary containing all the placeholder text as keys
        and the correct value.
    """

    d: Dict[str, str] = {}
    for index, exp in enumerate(_exps):
        matches = exp.findall(s)
        if DEBUG:
            print(exp, matches)
        for match in matches:
            ph = f"XASDF{str(index).zfill(2)}"
            s = s.replace(match, ph)
            if ph in d and VERBOSE:
                print(f"Error: {ph} is already in the dictionary")
                print("new", match)
                print("old", d[ph])
            d[ph] = match
    return d, s


def undo_sphinx_directives_protection(placeholders: dict, translated_text: str) -> str:
    for ph, value in placeholders.items():
        translated_text = translated_text.replace(ph, value)
        if DEBUG:
            print(ph, value)
            print(translated_text)
    return translated_text


if __name__ == "__main__":
    filename = args.filename
    if not os.path.isfile(filename):
        print(f"File not found: '{filename}'")
        sys.exit(-1)

    po = polib.pofile(filename)

    if args.translator.lower() == "google":
        translator = GoogleTranslator(source="en", target="tr")
    elif args.translator.lower() == "deepl":
        translator = DeeplTranslator(
            api_key=args.api_key, source="en", target="tr", use_free_api=True
        )
    else:
        raise ValueError("Invalid translator")

    for entry in po:
        # If the entry has already a translation, skip.
        if SKIP_TRANSLATED_ENTRIES and entry.msgstr:
            continue

        print("\nEN |", entry.msgid)
        placeholders, temp_text = protect_sphinx_directives(entry.msgid)
        if VERBOSE:
            print(temp_text)
            print(placeholders)

        # Translate the temporary text without sphinx statements
        translated_text = translator.translate(temp_text)

        # Recover sphinx statements
        real_text = undo_sphinx_directives_protection(placeholders, translated_text)
        print("TR |", real_text)

        # Replace the po file translated entry
        entry.msgstr = real_text

        # Add fuzzy flag so a real-human can review later
        entry.flags.append("fuzzy")

    # Save the file after all the entries are translated
    po.save()

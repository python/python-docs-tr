# Gettext Araçları

Bu belgede, ``gettext`` araçlarının nasıl kurulacağı açıklanmaktadır.

## Windows

Scoop, GNU araçlarını Windows'ta kullanmaya yarayan bir paket yöneticisidir. Scoop'u kullanarak ``gettext`` araçlarını yükleyebilirsiniz. Aşağıdaki komutları PowerShell'de çalıştırmanız gerekmektedir:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
scoop install gettext
```

## Linux

``apt`` paket yöneticisi kullanıyorsanız, gettext araçlarını şu komutla yükleyebilirsiniz:

```bash
sudo apt update
sudo apt install gettext
```

## macOS

``brew`` paket yöneticisi kullanıyorsanız, gettext araçlarını şu komutla yükleyebilirsiniz:

```zsh
brew update
brew install gettext
```

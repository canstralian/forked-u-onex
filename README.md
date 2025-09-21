# Onex

[![Python CI](https://github.com/canstralian/forked-u-onex/actions/workflows/python-ci.yml/badge.svg)](https://github.com/canstralian/forked-u-onex/actions/workflows/python-ci.yml)
[![Shell Script Lint](https://github.com/canstralian/forked-u-onex/actions/workflows/shellcheck.yml/badge.svg)](https://github.com/canstralian/forked-u-onex/actions/workflows/shellcheck.yml)
[![Release](https://github.com/canstralian/forked-u-onex/actions/workflows/release.yml/badge.svg)](https://github.com/canstralian/forked-u-onex/actions/workflows/release.yml)

***"onex a hacking tools library."***
Onex is a kali linux hacking tools installer for termux and other linux distribution. It's package manager for hacker's.
onex manage large number's of hacking tools that can be installed on single click. Using onex, you can install all hacking tools in Termux and other Linux based distributions.
onex can install **more than 370+ kali linux hacking tools**. use `onex install [tool_name]` command to install any hacking tool.

<br>
<p align="center">
<img width="47%" src="doc/Screenshot_2019-12-01-12-10-02-1.png"/>
<img width="46%" src="doc/Screenshot_2019-12-01-12-09-26-1.png"/>
</p>

------------------------------------------------------------------------

## Operating System Requirements

onex works on any of the following operating systems:<br>
- **Android** (Using the Termux App) <br>
- **Linux** (Linux Based Systems) <br>

------------------------------------------------------------------------

## How to Install

To get started with the Onex Pentesting Lab, you need to install the Onex tool. These instructions are for Debian-based Linux distributions (like Ubuntu or Kali Linux) and Termux on Android.

#### 1. Update Your Package Lists

First, open your terminal and update your system's package lists to ensure you have the latest versions:

```bash
apt update
```

#### 2. Install Git

Next, you'll need to install Git, which is a version control system used to download the Onex repository:

```bash
apt install git
```

#### 3. Clone the Onex Repository

Now, you can clone the Onex repository from GitHub to your local machine:

```bash
git clone https://github.com/canstralian/forked-u-onex.git
```

#### 4. Make the Installation Script Executable

After cloning the repository, you need to give the installation script the necessary permissions to run:

```bash
chmod +x forked-u-onex/install
```

#### 5. Run the Installation Script

Finally, you can run the installation script to set up Onex on your system:

```bash
sh forked-u-onex/install
```

If the above command doesn't work, you can try running it with `./` at the beginning:

```bash
./forked-u-onex/install
```

Once the installation is complete, you can start using Onex to install and manage your security tools. For a full list of commands and options, you can use the `onex help` command.

------------------------------------------------------------------------

## How to use onex ?

### CLI Mode :
`onex -h` or `onex help` for help.

Options :
- `onex install [tool_name]` install any tool.
- `onex -i [tool_name]` install any tool.
- `onex search [tool_name]` search any tool.
- `onex -s [tool_name]` search any tool.
- `onex list` list all tools.
- `onex list -a` list all tools.
- `onex -l` list all tools.
- `onex -l -a` list all tools.
- `onex help` get help.
- `onex -h` get help.

### Menu Mode :

`onex start` to start onex menu mode.

Enter a Number for a specific output:
- (1) : To show all available tools and type the number of a tool which you want to install.
- (2) : To show tools category.
- (3) : If you want to update onex.
- (4) : If you want to know About Us.
- (5) : To exit the tool.

------------------------------------------------------------------------

**Warning**

Please use this tool at your own risk!


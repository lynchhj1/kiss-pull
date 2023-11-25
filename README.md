# kiss-pull

<!-- TABLE OF CONTENTS -->

<summary>Table of Contents</summary>
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
  </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
</ol>


<!-- ABOUT THE PROJECT -->
## About The Project

This project is a python conversion of a shell script I wrote a few years ago.  This script will download the html for a manga issue/chapter, use it to download all of the images, and zip into a cbz.


<!-- GETTING STARTED -->
## Getting Started

In order to use this script you need to dowload the python script and install a few modules if you don't have them already.

### Prerequisites

Beautiful soup should be the only module you need to install. You can use either of the below commands to install it.
* python modules through apt
  ```sh
  sudo apt install python3-bs4
  ```
* python modules through pip
  ```sh
  pip3 install beautifulsoup4
  ```

### Installation

Download the python script [here](manga-pull.py)


<!-- USAGE EXAMPLES -->
## Usage

The below command is an example of how to use the script. This will create a cbz in the path where you run it.

  ```sh
  python3 manga-pull.py https://kissmanga.org/chapter/manga-mv990156/chapter-0.1
  ```
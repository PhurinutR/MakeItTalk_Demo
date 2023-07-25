# MakeItTalk Demo
### Tutorial for Technologies Making a Face Picture Talk

## Requirements and Warning

| **Requirements**     | **Tool Name**                                           | **URL**                                                                                                                                                      |
| -------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Operating System     | Linux or Windows                                        |                                                                                                                                                              |
| Programming Language | Python version 3.6 for Linux or version 3.7 for Windows | [https://www.python.org/downloads/](https://www.python.org/downloads/)                                                                                       |
| Framework            | PyTorch version >= 1.10                                 | [https://pytorch.org/](https://pytorch.org/)                                                                                                                 |
| Environment Manager  | Conda (Anaconda or Miniconda)                           | [https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) |

### <center><span style="color: red;">⚠️WARNING⚠️</span></center>
<center><span style="color: red;">As there are many large files needed to use in order to start this tutorial, please prepare up to 6 GB of free space in your computer before starting.</span></center>

## MakeItTalk Practical Guide: How to Make Your First Talking Face

### MakeItTalk at A Glance

MakeItTalk is a method to generate a talking head from two inputs: a static face and the audio. These two ingredients are used to produce a video of that input person face speaking the content in the audio while making facial expression corresponding to the content and the speaking identity. Therefore, by using MakeItTalk, not only the mouth of the input face is moving, but his face as a whole is also moving to express non-verbal expression giving more natural talking head synchronously to the input audio.

 ![image](https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/b9485ab9-12e0-4796-a495-7c4aec1876b1)

Throughout this practical guide section, you will learn how to turn a picture of a face and an audio into a video using the GUI provided.

### Installation Procedure

#### 1. Open a Terminal on Ubuntu or Anaconda Prompt on Windows
#### 2. Environment Setup

**For Linux users**
Create a dedicated conda environment with a desired name (e.g: makeittalk_env) and python 3.6 installation by typing the follow in the Terminal.

~~~
conda create -n makeittalk\_env python=3.6
~~~

**For Windows users**
Create a dedicated conda environment with a desired name (e.g: makeittalk_env) and python 3.7 installation by typing the follow in the Anaconda prompt.

~~~
conda create -n makeittalk_env python=3.7
~~~

Conda manager will download the necessary packages and will prompt you with a **Proceed ([y]/n)?** Type **y** to proceed with the downloads and installation.

Then, activate the newly created environment (makeittalk_env or whatever you have used) by typing the following:

~~~
conda activate makeittalk_env
~~~

The activated environment will now appeared in a parenthesis with your environment name inside at the beginning of your command lines as illustrated below:

~~~
(makeittalk_env) [Your Computer Name]:~$
~~~

#### 3. PyTorch Installation

The framework upon which MakeItTalk was trained was PyTorch, hence you need to install PyTorch by visiting its official site (https://pytorch.org/) and selecting the configuration that matches your system. For instance, below is a configuration for a Windows operating system that has a GPU card compatible with CUDA 11.7

<img width="452" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/ffe22f7f-0381-4ace-9214-e6e6be2dc454">

However, to avoid clashes due to packages version change, it is highly recommended to use the following command to install PyTorch.

~~~
conda install pytorch==1.10.2 torchvision torchaudio cudatoolkit=11.3 -c pytorch -c nvidia
~~~

#### 4. Multimedia Processing Package Installation
An open source package named FFmpeg is required for audio and video processing to achieve the talking-head animation. Type the following command in a Linux Terminal to install ffmpeg:

~~~
sudo apt-get install ffmpeg
~~~

If your operating system is Windows, following the instructions provided in this URL: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/ for FFmpeg installation on Windows.

#### 5. Get The Code to Interact with MakeItTalk
**Note:** If you are given the code from your supervisor, please skip this step, and depending on your operation system, copy either **MakeItTalk_Linux** or **MakeItTalk_Windows** directory to your preferred working directory.

In order to get the code and try using MakeItTalk via the GUI, go to this GitHub URL: https://github.com/PhurinutR/MakeItTalk_Demo and Download **MakeItTalk_Demo** repository by clicking **Code ⇾ Download ZIP** as shown in the picture below.

<img width="451" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/3a100d95-9c8a-4875-92dc-2386bbc72b60">

After downloading, extract **MakeItTalk_Demo-main.zip** and check what you have inside. At this point, you should be able to find 2 directories under the **MakeItTalk_Demo-main** folder.

<img width="362" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/d08a1827-b8ee-4762-898d-c707aa6a0ce7">

If you are using Linux operation system select **MakeItTalk_Linux** directory, cut, and paste it to a directory that you want to work on, for example, **Home** directory, or others. Similarly, if you are using Windows select **MakeItTalk_Windows** directory, cut, and paste it to a directory that you want to work on, for example, **D:** drive, **C:** drive, or others.

**Note:** feel free to remove the **MakeItTalk_Demo-main** folder after cutting either **MakeItTalk_Linux** or **MakeItTalk_Windows** to your working directory.


#### 6. Python Packages
Next, through the terminal or Anaconda prompt opened earlier, navigate yourself to **MakeItTalk_Linux** or **MakeItTalk_Windows** that you just pasted it under your working directory using the command below.

~~~
cd [path to your working directory]/[replace this with MakeItTalk_Linux or MakeItTalk_Windows]
~~~

Under both **MakeItTalk_Linux** and **MakeItTalk_Windows**, requirements.txt file is provided to help you install the packages that you need.

<img width="432" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/9d31a2d9-6401-41c9-ae67-2e2af23b88a1">


Type the command below in the terminal or Anaconda prompt to install the python packages in the requirements.txt file.

~~~
pip install –r requirements.txt
~~~

#### 7. Download Weighting of Pre-trained Models
**Note:** If you are given the code from your supervisor, please skip this step.

Go back to the GitHub **MakeItTalk_Demo** repository and check out the menu called **“Releases”**.

<img width="432" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/78f6237f-0090-497b-b119-7f1e2bca8f08">

Here, you should find two releases called “ckpt” and “checkpoints”.

<img width="440" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/169fa922-f7cb-486b-ac1a-3d12906c071c">

For ckpt, if you are using Linux operation system, download the two files shown below to **MakeItTalk_Linux/examples/ckpt** directory, or, if you are using Windows, you can download them to **MakeItTalk_Windows/examples/ckpt** directory.

<img width="411" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/2c70eedb-c2da-4a06-a396-c828d370f054">

In the same manner, download the five files below to **MakeItTalk_Linux/checkpoints** directory if you are using Linux, or to **MakeItTalk_Windows/checkpoints** directory if you are using Windows.

<img width="409" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/6a961b3a-6766-4614-8790-12b552d9cb83">

### Animate Your Photo

Now, everything has been setup and ready to use. As mentioned earlier that you will interact with MakeItTalk via GUI, thus this GUI has been created and provided under both **MakeItTalk_Linux** and **MakeItTalk_Windows**. To start using it, type command below in your terminal or Anaconda prompt.

~~~
python GUI.py
~~~

This command will start up the program which act like a palette used to pick a face and pick an audio to animate it.

<img width="247" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/268269a2-a824-4f85-a4f0-944a66eef5f0">

On the pink menu on the left, you can choose which static face you want to make it talk, and on the light blue menu on the right, you can choose an audio that you want to that face to talk. After done with choosing face and sound option, click “Make It Talk!!” button to start animating the select face.

<img width="451" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/f407aaba-e7f8-4e85-b4b6-846e87041f4d">

While the program is calculating, the loading bar will show up and, on the terminal or Anaconda prompt, intermediate results and information will be printed out to report the calculation process. Right after it finish inferencing, you will see the “Notice” window prompt up telling that in the inferencing process is finish. Moreover, besides the “Notice” window, the result video should be prompted up to show you the outcome of the taking head.

<img width="451" alt="image" src="https://github.com/PhurinutR/MakeItTalk_Demo/assets/106614460/4a0721e0-7e82-435a-9c03-d055b177520a">

You could try MakeItTalk with other faces or other sounds by simply clicking other face or audio and clicking “Make It Talk!!” button again. After several tries, one important thing that you can notice from the result video is that the motion of the speaker in the result doesn’t appear only on his or her mouth but the entire face like face turning, eyes blinking, head nodding and other facial expressions are all there to fulfill realism to the generated talking head.

To crystalize the concept of how MakeItTalk turns the input static portrait and audio into speaker-aware talking head animation, in the next section, the mechanism behind MakeItTalk will be explained along with some demonstrations to illustrate what is generated inside in each process.

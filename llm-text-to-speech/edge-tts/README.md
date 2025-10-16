{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Edge-TTS：微软推出的，免费、开源、支持多种中文语音语色的AI工具\n",
    "\n",
    "> Edge-TTS是由微软推出的文本转语音Python库，通过微软 Azure Cognitive Services转化文本为自然语音。适合需要语音功能的开发者，GitHub上超3000星。作为国内付费TTS服务的替代品，Edge-TTS支持40多种语言和300种声音，提供优质的语音输出，满足不同开发需求。\n",
    "\n",
    "### 1.安装部署\n",
    "\n",
    "首先，你需要通过Python包管理工具pip来安装Edge-TTS库。只需在命令行中输入以下命令（没有python环境的自行配置一下）：\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "!pip install edge-tts\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "如果只想使用edge-tts和edge-playback命令，最好使用 pipx："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pipx install edge-tts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "安装完成后，你就可以开始使用Edge-TTS来将文本转换为语音了。Edge-TTS支持多种语言和不同的声音选项，你可以根据需要选择合适的声音。\n",
    "\n",
    "### 2.文本转语音\n",
    "\n",
    "我们先来个hello world，只需要一行代码！\n",
    "\n",
    "```python\n",
    "edge-tts --text \"hello world\" --write-media hello.mp3\n",
    "```\n",
    "\n",
    "执行完毕之后，会在你执行的目录下，生成hello.mp3文件\n",
    "\n",
    "如果你想立即播放带有字幕的内容，可以使用以下edge-playback命令：\n",
    "\n",
    "```python\n",
    "edge-playback --text \"Hello, world!\"\n",
    "```\n",
    "\n",
    "注意以上需要安装mpv命令行播放器。所有命令也都edge-tts可以工作。edge-playback\n",
    "\n",
    "### 3.支持的语言和音色\n",
    "\n",
    "edge-tts支持英语、汉语、日语、韩语、法语等40多种语言，共300多种可选声音，执行以下命令查询：\n",
    "\n",
    "```python\n",
    "edge-tts --list-voices\n",
    "```\n",
    "\n",
    "查询结果中的Gender为声音的性别，Name为声音的名字，如zh-CN-YunjianNeural，其中zh表示语言，CN表示国家或地区，可以根据需求选择不同的声音。\n",
    "\n",
    "使用--voice参数来指定声音名称，下面我使用zh-CN-YunyangNeural声音来合成一个中文音频。\n",
    "\n",
    "edge-tts --voice zh-CN-YunyangNeural --text \"大家好，欢迎关注语音之家，语音之家是一个助理AI语音开发者的社区。\" --write-media hello_in_cn.mp3\n",
    "\n",
    "### 4.调整语速、音量和音调\n",
    "\n",
    "可以对生成的语音进行细微修改。\n",
    "\n",
    "```shell\n",
    "$ edge-tts --rate=-50% --text \"Hello, world!\" --write-media hello_with_rate_halved.mp3 --write-subtitles hello_with_rate_halved.vtt\n",
    "$ edge-tts --volume=-50% --text \"Hello, world!\" --write-media hello_with_volume_halved.mp3 --write-subtitles hello_with_volume_halved.vtt\n",
    "$ edge-tts --pitch=-50Hz --text \"Hello, world!\" --write-media hello_with_pitch_halved.mp3 --write-subtitles hello_with_pitch_halved.vtt\n",
    "```\n",
    "\n",
    "此外，必须使用 --rate=-50% 而不是 --rate -50%（注意等号的缺失），否则 -50% 将被解释为另一个参数。\n",
    "\n",
    "### 5.使用代码转换\n",
    "\n",
    "上面都是用命令转换，我们也可以写代码调用，开发http接口来提供语音合成服务。\n",
    "\n",
    "以下是一个代码示例，将代码保存到一个文件中，如tts.py。\n",
    "\n",
    "```python\n",
    "#!/usr/bin/env python3\n",
    "    \n",
    "\"\"\"\n",
    "Basic example of edge_tts usage.\n",
    "\"\"\"\n",
    "    \n",
    "import asyncio\n",
    "    \n",
    "import edge_tts\n",
    "    \n",
    "TEXT = \"大家好，欢迎关注语音之家，语音之家是一个助理AI语音开发者的社区。\"\n",
    "VOICE = \"zh-CN-YunyangNeural\"\n",
    "OUTPUT_FILE = \"d:/test.mp3\"\n",
    "    \n",
    "    \n",
    "async def amain() -> None:\n",
    "    \"\"\"Main function\"\"\"\n",
    "    communicate = edge_tts.Communicate(TEXT, VOICE)\n",
    "    await communicate.save(OUTPUT_FILE)\n",
    "    \n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    loop = asyncio.get_event_loop_policy().get_event_loop()\n",
    "    try:\n",
    "        loop.run_until_complete(amain())\n",
    "    finally:\n",
    "        loop.close()\n",
    "```\n",
    "\n",
    "关于 edge-playback 命令的说明\n",
    "\n",
    "edge-playback 实际上是 edge-tts 的一个封装，用于播放生成的语音。它接受与 edge-tts 选项相同的参数。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

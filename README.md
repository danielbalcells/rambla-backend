This repo contains the very simple backend used to power Rambla, a walking meditation companion app I created in the fall of 2023. You can read more about Rambla [here](https://danibalcells.com/2023/10/17/rambla/).

In a nutshell, Rambla is an iOS app that helps the user explore complex topics by breaking them down into simpler questions, which are represented as nearby locations in a map. As the user walks to these locations and answers the questions, more questions appear, based on the overall meditation.

![](https://danielbalcells.files.wordpress.com/2023/10/img_2712.png?w=300) ![](https://danielbalcells.files.wordpress.com/2023/10/img_2713.png?w=300) ![](https://danielbalcells.files.wordpress.com/2023/10/img_2704.png?w=300)
![](https://danielbalcells.files.wordpress.com/2023/10/img_2707.png?w=300) ![](https://danielbalcells.files.wordpress.com/2023/10/img_2709.png?w=300) ![](https://danielbalcells.files.wordpress.com/2023/10/img_2710.png?w=300)


The backend works as follows:
- It receives requests from the iOS app containing the user's input (initial topic and subsequent replies), and responds with simple, relevant questions.
- `backend.py` initializes a Flask server (good enough for personal/testing use) and a custom LLM chain.
- `chain.py` contains the implementation of the LLM chain. Specifically, Rambla uses theory-of-mind reasoning to produce an answer in two steps: it first generates a hypothesis about the user's mental state based on their input, and then produces a list of helpful questions based on both the user's input and the hypothesis.
- The code for the iOS app is [here](https://github.com/danielbalcells/rambla-app/tree/main). I've never coded for iOS and wrote the entire frontend with the help of ChatGPT, so apologies in advance for the mess.

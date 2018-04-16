# Freewill
Freewill proof of concepts written in Python.
<hr>
The idea is an implementation of the studies here:

```
http://www.livescience.com/46411-free-will-is-background-noise.html
http://www.independent.co.uk/news/science/free-will-could-be-the-result-of-background-noise-in-the-brain-study-suggests-9553678.html
```

We initialize an array with random numbers that act as brain noise.<br>
This noise is constantly changing before a new decision is made<br>
The idea is to factor preferences into brain noise to allow for<br>
the program to make a decision "freely".<br>
It is highly recommended you feed the noise using a TRNG (True RNG)<br>
for the free-ist possible decisions to be made by the program.<br><hr>
What can we done with this?<br>
It's only a proof-of-concept project at the moment but I do plan on<br>
expanding it into an AI.<br>
I suppose you could do the same.<br><hr>
Have any questions or disagree with the idea?<br>
Then fork the project or find a way to contact me.<br>
I'd be glad to talk about this.
<hr>
To configure this simply change the preferences {} dictionary.<br>
4 and 4 means no preference. Changing the 4 to let's say 5<br>
adds preference into the noise.

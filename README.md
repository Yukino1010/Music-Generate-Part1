# Music-Generate-Part1

## Introduce
RNN is a kind of sequence to sequence model, it can solve a lot of NLP problems such as  Machine translation 、 Summarization 、
and even can generate article. <br>
This time I am going to use RNN to generate music, similar to Article generation we can convert music
into notes and durations then we can treat them as the input of RNN. <br>
But the problem of RNN is that it only allows fixed length of inpurt sequence, so I introduced Attention mechanism to solve this problem.

## Network Structure
![image](https://github.com/Yukino1010/Music-Generate-Part1/blob/master/model/malti_head_model_structure.png)


### network design
- use Bidirectional LSTM with 256 units
- use malti-head attention


## Data
The data contains 24 anime musics <br>
and is collected from [https://www.midiclouds.com/forum-4-1.html]
## Result

[https://github.com/Yukino1010/Music-Generate-Part1/blob/master/output/first.mid]<br>
[https://github.com/Yukino1010/Music-Generate-Part1/blob/master/output/second.mid]<br>
[https://github.com/Yukino1010/Music-Generate-Part1/blob/master/output/third.mid]<br>

Although the result looks terrible and had been overfitting, <br>
But it did capture some of the information in the original data, that makes it a bit like real music.
## References
davidADSP GDL_code[https://github.com/davidADSP/GDL_code]

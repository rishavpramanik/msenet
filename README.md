# Mean and standard deviation based ensemble network for cervical cancer detection
"MSENet: Mean and standard deviation based ensemble network for cervical cancer detection" published in Engineering Applications of Artificial Intelligence, Elsevier (Aug 2023)
```
@article{pramanik2023msenet,
  title={MSENet: Mean and standard deviation based ensemble network for cervical cancer detection},
  author={Pramanik, Rishav and Banerjee, Bihan and Sarkar, Ram},
  journal={Engineering Applications of Artificial Intelligence},
  volume={123},
  pages={106336},
  year={2023},
  publisher={Elsevier}
}
```
**MSENet: Mean and standard deviation based ensemble network for cervical cancer detection**

Find the original paper [Here](https://doi.org/10.1016/j.engappai.2023.106336).

# Datasets Links
1. [SIPaKMeD SCI Pap Smear Images](https://www.cs.uoi.gr/~marina/sipakmed.html)
2. [Mendeley LBC](https://data.mendeley.com/datasets/zddtpgzv63/4)

# Instructions to run the code
Required directory structure:
(Note: ``train`` and ``test`` contains subfolders representing classes in the dataset.)
```
+-- data
|   +-- train
|   |   +--class A
|   |   +--class B
|   |   ...
|   +-- test
|   |   +--class A
|   |   +--class B
|   |   ...
+-- main.py
```
1. Download the repository and install the required packages:
```
pip3 install -r requirements.txt
```
2. The main file is sufficient to run the experiments.
Then, run the code using linux terminal as follows:

```
python3 main.py --data_directory "data"
```

Available arguments:
- `--num_epochs`: Number of epochs of training. Default = 75
- `--learning_rate`: Learning Rate. Default = 0.0001
- `--batch_size`: Batch Size. Default = 32
- `--path`: Data Path. Default= './'
- `--kfold`: K-Fold, to perform K fold cross validation. Default= 5

3. Please don't forget to edit the above parameters before you start

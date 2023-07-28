# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:51:59 2023

@author: CTTC
"""
#deep learning is a feature of machine leraning, where automatic feature extraction can be done\
#deep learning is a type of supervised learning, can also be semi-supervised
#the inputs represent 'dendrites' of actual neuron
#a single neuron in deep learning is perceptron, the smallest component of ANN
#many perceptrons make up artificial neural network(ANN)

#each time, epoch means each run

#each input(x) has a weightage(w), so that the strenght can be used for the final output, it is automatically taken up by the model
#Weights set the standards for the neuron's signal strength. 
#This value will determine the influence input data has on the output product.
#weights(w) are initially taken at random for the first epoch
#according to the error in the first random epoch, the second epoch is then adjusted with the weightage values, based on the errors of the predicted data
#the predicted error is taken into account that the how much error was encountered in the previous epoch`

#in deep learning models, training is very slow, by testing is very fast. 
#'bais factor(b)' is used to move the activation function up or down the node, so that all the featuers are taken into account, so that all possible predictions are tested
#'bais factor' for each hidden layer in one single epoch, it updates along with the 'weightage' during back propagation.
#each neuron is connected to the next neuron using 'channels'

#activation function-> works inside the hidden layer 
#An Activation Function decides whether a neuron should be activated or not. 
#This means that it will decide whether the neuron's input to the network is important or not in the process of prediction using simpler mathematical operations.

#Various acticvation functions are:
# 1) Sigmoid-> 0-1 range, This function takes any real value as input and outputs values in the range of 0 to 1. 
#The larger the input (more positive), the closer the output value will be to 1.0.
#whereas the smaller the input (more negative), the closer the output will be to 0.0.

# 2) tanh-> -1 to +1 range,Tanh Activation is an activation function used for neural networks: f ( x ) = e x − e − x e x + e − x. 
#Historically, the tanh function became preferred over the sigmoid function as it gave better performance for multi-layer neural networks.

# 3) Linear-> continous values, The linear activation function, also known as "no activation," or "identity function" (multiplied x1.0)
#It is where the activation is proportional to the input. 
#The function doesn't do anything to the weighted sum of the input.
#It simply spits out the value it was given. Linear Activation Function

# 4) ReLu-> 0 to n raneg, negatives are converted to 0, most popular
#The rectified linear activation function or ReLU for short is a piecewise linear function 
#It will output the input directly if it is positive, otherwise, it will output zero.

#' x1w1 + x2w2 +......+ xnwn =' happens inside the cell body-> summation of products of inputs and their weightage-> transfer function
# the bais factor(b) is then added to the 'transfer function' to form the 'activation function'
#' b + x1w1 + x2w2 +......+ xnwn = activation function', brings non-linearity, or else the variations won't be tried
#this combines the features and makes prediction based on it
#each input node refers to separate features and attributes of the input
#we use 'keras' and 'tensorflow' for deep learning

#from input to output is the forward propagation-> trains data
#from output to input is the backward propagation-> gives feedback of the current prediction
#'cost function' gives the amount of error term, and is used to rectify the 'bais factor' and the 'input weightages'

#gradient boosting is used in deep learning for reaching the accuracy and speeding up
#the learning rate is used to gives the speed of learning
#slow learning rate can reach the 'point of convergence'-> minimum loss, easily
#fast learning skips the 'point of convergence' and moves forward likea pendulum, and never reaches the 'point of convergence'

#'Cross Entropy' is an error finding model, same as 'confusion matirx' of classical models, 'Error Function'
#'-[log(P(Yes))+log(P(No))]'-> is single cross entropy, higher values of cross entropy represents higher error.
#'-[Σ yln(P)+(1-y)(ln(1-P))]'-> Total Cross Entropy,'y' represents one category, while 'P' represents its happening probability

#'Gradient Descent' -> derivative with respect to weigth function, and subtracts it to the activation function, to minimize loss function
#Works good on binary cross entropy, in the end the hyperline is linear, linearly separable data

#'Softmax' function is used for multi-class data set, multiple output categories
#'Softmax' is applied to the output layer, so that the scores are converted to probabilities
#the higher probabilitiy is the prediction
#the relative magnitude must be maintained and sum of all the probabilites must result to 1.

#over-trained models results to sum of probabilities more than 1.
#for over-trained models, we use the regularization factors for getting the best fit model.


import random
input_x=[[1,4],[2,5],[5,1],[4,2]]
y=[19,26,19,20]
theta=[1,1]
loss=10
step_size=0.01
eps=0.0001
max_iters=10000
error=0
iter_count=0

err1=[0,0,0,0]
err2=[0,0,0,0]

while(loss>eps and iter_count<max_iters):
    loss=0
    err1sum=0
    err2sum=0
    for i in range(4):
        pred_y=theta[0]*input_x[i][0]+theta[1]*input_x[i][1]
        err1[i]=(pred_y-y[i])*input_x[i][0]
        err1sum=err1sum+err1[i]
        err2[i]=(pred_y-y[i])*input_x[i][1]
        err2sum=err2sum+err2[i]
    theta[0]=theta[0]-step_size*err1sum/4
    theta[1]=theta[1]-step_size*err2sum/4
    for i in range(4):
        pred_y=theta[0]*input_x[i][0]+theta[1]*input_x[i][1]
        error=(1/(2*4))*(pred_y-y[i])**2
        loss=loss+error
    iter_count+=1
    print('iters_count:',iter_count)
print('theta:', theta)
print('final_loss:',loss)
print('iters:',iter_count)

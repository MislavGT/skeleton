import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

plt.style.use('seaborn-poster')

##### konstante
NUI_SKELETON_POSITION_HIP_CENTER = 0
NUI_SKELETON_POSITION_SPINE = 1
NUI_SKELETON_POSITION_SHOULDER_CENTER = 2
NUI_SKELETON_POSITION_HEAD = 3
NUI_SKELETON_POSITION_SHOULDER_LEFT = 4
NUI_SKELETON_POSITION_ELBOW_LEFT = 5
NUI_SKELETON_POSITION_WRIST_LEFT = 6
NUI_SKELETON_POSITION_HAND_LEFT = 7
NUI_SKELETON_POSITION_SHOULDER_RIGHT = 8
NUI_SKELETON_POSITION_ELBOW_RIGHT = 9
NUI_SKELETON_POSITION_WRIST_RIGHT = 10
NUI_SKELETON_POSITION_HAND_RIGHT = 11
NUI_SKELETON_POSITION_HIP_LEFT = 12
NUI_SKELETON_POSITION_KNEE_LEFT = 13
NUI_SKELETON_POSITION_ANKLE_LEFT = 14
NUI_SKELETON_POSITION_FOOT_LEFT = 15
NUI_SKELETON_POSITION_HIP_RIGHT = 16
NUI_SKELETON_POSITION_KNEE_RIGHT = 17
NUI_SKELETON_POSITION_ANKLE_RIGHT = 18
NUI_SKELETON_POSITION_FOOT_RIGHT = 19

NUI_SKELETON_POSITION_COUNT = 20

HIP_CENTER = 0
SPINE = 1
SHOULDER_CENTER = 2
HEAD = 3
SHOULDER_LEFT = 4
ELBOW_LEFT = 5
WRIST_LEFT = 6
HAND_LEFT = 7
SHOULDER_RIGHT = 8
ELBOW_RIGHT = 9
WRIST_RIGHT = 10
HAND_RIGHT = 11
HIP_LEFT = 12
KNEE_LEFT = 13
ANKLE_LEFT = 14
FOOT_LEFT = 15
HIP_RIGHT = 16
KNEE_RIGHT = 17
ANKLE_RIGHT = 18
FOOT_RIGHT = 19

nui_skeleton_conn = np.matrix([ 
	[HIP_CENTER, SPINE],
	[SPINE, SHOULDER_CENTER],
	[SHOULDER_CENTER, HEAD],
	#Left arm ...
	[SHOULDER_CENTER, SHOULDER_LEFT],
	[SHOULDER_LEFT, ELBOW_LEFT],
	[ELBOW_LEFT, WRIST_LEFT],
	[WRIST_LEFT, HAND_LEFT],
        #Right arm ...
	[SHOULDER_CENTER, SHOULDER_RIGHT],
	[SHOULDER_RIGHT, ELBOW_RIGHT],
	[ELBOW_RIGHT, WRIST_RIGHT],
	[WRIST_RIGHT, HAND_RIGHT],
	#Left leg ...
	[HIP_CENTER, HIP_LEFT],
	[HIP_LEFT, KNEE_LEFT],
	[KNEE_LEFT, ANKLE_LEFT],
	[ANKLE_LEFT, FOOT_LEFT],
	#Right leg ...
	[HIP_CENTER, HIP_RIGHT],
	[HIP_RIGHT, KNEE_RIGHT],
	[KNEE_RIGHT, ANKLE_RIGHT],
	[ANKLE_RIGHT, FOOT_RIGHT]
])

####kraj konstanta

def skel_vis(X, tidix):
    
    assert tidix >= 1
    assert tidix <= X.shape[0]

    xyz_ti=X[tidix,:]

    skel=xyz_ti.reshape( NUI_SKELETON_POSITION_COUNT, 4)
 
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_title('3D Skeleton')
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)
    
    ax.scatter3D(X[:,0], X[:,2], X[:,1], zdir='z', c= 'red');

    for i in range(nui_skeleton_conn.size//2):
        prva = nui_skeleton_conn[i, 0];
        druga = nui_skeleton_conn[i, 1];
    
        ax.plot([X[prva , 0], X[druga , 0]], [X[ prva, 2], X[druga, 2 ]],zs=[X[prva, 1], X[druga, 1]])
    
    plt.show()


data_start = "643775645 0.067645 0.142099 2.710277 1.000000 0.070329 0.210310 2.712830 1.000000 0.084185 0.557534 2.704327 1.000000 0.072051 0.725057 2.677813 1.000000 -0.090970 0.428102 2.709811 1.000000 -0.137749 0.179182 2.729523 1.000000 -0.137719 -0.020337 2.664578 1.000000 -0.138439 -0.097101 2.654370 1.000000 0.231562 0.421160 2.716174 1.000000 0.251021 0.208005 2.725669 1.000000 0.261632 0.003032 2.693177 1.000000 0.256333 -0.087692 2.676868 1.000000 -0.007914 0.071922 2.704566 1.000000 -0.045638 -0.394799 2.758982 1.000000 -0.074465 -0.772465 2.812992 1.000000 -0.069252 -0.837524 2.758063 1.000000 0.137314 0.067924 2.712796 1.000000 0.152791 -0.410378 2.771634 1.000000 0.155838 -0.768063 2.817297 1.000000 0.155735 -0.845933 2.782465 1.000000 643875762 0.057629 0.132074 2.715119 1.000000 0.058785 0.202508 2.715816 1.000000 0.062076 0.555270 2.703448 1.000000 0.062613 0.725752 2.677764 1.000000 -0.104866 0.429053 2.709782 1.000000 -0.146319 0.188848 2.730810 1.000000 -0.144568 -0.013846 2.667759 1.000000 -0.149526 -0.106410 2.659052 1.000000 0.224260 0.422361 2.718132 1.000000 0.233154 0.153809 2.738293 1.000000 0.253427 -0.048725 2.690672 1.000000 0.252107 -0.140691 2.676212 1.000000 -0.017840 0.059163 2.710669 1.000000 -0.050624 -0.402983 2.761949 1.000000 -0.074324 -0.772653 2.812402 1.000000 -0.074026 -0.837361 2.755724 1.000000 0.130256 0.056987 2.718962 1.000000 0.149835 -0.409458 2.774297 1.000000 0.156079 -0.770086 2.821153 1.000000 0.165536 -0.849109 2.788511 1.000000 643942827 0.049958 0.134640 2.716837 1.000000 0.050018 0.204727 2.715758 1.000000 0.048824 0.554492 2.699593 1.000000 0.050882 0.723903 2.673098 1.000000 -0.112717 0.430198 2.707458 1.000000 -0.155016 0.187535 2.732381 1.000000 -0.152336 -0.013181 2.670168 1.000000 -0.159285 -0.102509 2.661426 1.000000 0.212765 0.421603 2.720680 1.000000 0.229599 0.189465 2.736726 1.000000 0.246425 -0.015506 2.703542 1.000000 0.242607 -0.107621 2.687448 1.000000 -0.023217 0.061695 2.712384 1.000000 -0.053958 -0.402048 2.762833 1.000000 -0.074671 -0.772910 2.810384 1.000000 -0.071285 -0.836142 2.751503 1.000000 0.122120 0.060306 2.722367 1.000000 0.145679 -0.409161 2.774874 1.000000 0.156634 -0.769186 2.820068 1.000000 0.153615 -0.837327 2.766922 1.000000 644209843 0.032382 0.137977 2.721363 1.000000 0.031546 0.207223 2.716022 1.000000 0.026006 0.553666 2.693917 1.000000 0.017828 0.723180 2.664454 1.000000 -0.145174 0.428416 2.704956 1.000000 -0.180946 0.178025 2.735317 1.000000 -0.180110 -0.032977 2.684615 1.000000 -0.179684 -0.104726 2.671677 1.000000 0.186280 0.428237 2.721658 1.000000 0.215923 0.188245 2.750278 1.000000 0.236371 -0.019220 2.723653 1.000000 0.229802 -0.114142 2.700658 1.000000 -0.041272 0.062250 2.717049 1.000000 -0.061606 -0.400205 2.768776 1.000000 -0.076844 -0.774930 2.813102 1.000000 -0.062876 -0.838935 2.755399 1.000000 0.107446 0.064635 2.730769 1.000000 0.133579 -0.408859 2.772498 1.000000 0.158666 -0.778940 2.797831 1.000000 0.157430 -0.858095 2.761027 1.000000 644609724 0.063590 0.135254 2.709393 1.000000 0.063988 0.204893 2.706232 1.000000 0.067548 0.553682 2.699886 1.000000 0.057099 0.723996 2.674155 1.000000 -0.100361 0.422092 2.705294 1.000000 -0.125618 0.167242 2.719010 1.000000 -0.122732 -0.037494 2.652660 1.000000 -0.128445 -0.133758 2.640640 1.000000 0.223239 0.424865 2.713080 1.000000 0.254745 0.179891 2.724673 1.000000 0.273808 -0.028537 2.680740 1.000000 0.260933 -0.123977 2.667724 1.000000 -0.011274 0.062440 2.704736 1.000000 -0.042731 -0.404968 2.761726 1.000000 -0.076780 -0.775478 2.807539 1.000000 -0.064899 -0.842078 2.751544 1.000000 0.137938 0.061399 2.712743 1.000000 0.145085 -0.420092 2.768990 1.000000 0.155106 -0.785409 2.801756 1.000000 0.164295 -0.859720 2.755869 1.000000"
data_start = data_start.split(' ')
X = np.matrix(data_start, dtype=float)
X = X.reshape(5,81)
X = X[: , 1:]


data = np.empty(X.shape[0], dtype=np.matrix)
for i in range (X.shape[0]):
    Y = X[i , :]
    Y=Y.reshape( NUI_SKELETON_POSITION_COUNT, 4)
    data[i]=Y

def animate_scatters(iteration, data, scatters):
    """
    Update the data held by the scatter plot and therefore animates it.
    Args:
        iteration (int): Current iteration of the animation
        data (list): List of the data positions at each iteration.
        scatters (list): List of all the scatters (One per element)
    Returns:
        list: List of scatters (One per element) with new coordinates
    """
    print(data[iteration][0,0:1])
    print(data[iteration][0,2:3])
    print(data[iteration][0,1:2])
    for i in range(data[0].shape[0]):
        scatters[i]._offsets3d = (data[iteration][i,0:1], data[iteration][i,2:3], data[iteration][i,1:2])
    print(scatters)
    return scatters

fig = plt.figure()
ax = p3.Axes3D(fig)

scatters = [ ax.scatter(data[0][i,0:1], data[0][i,2:3], data[0][i,1:2]) for i in range(data[0].shape[0]) ]
print(scatters)
iterations = len(data)

# Setting the axes properties
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Animated Scatter Example')

ani = animation.FuncAnimation(fig, animate_scatters, iterations, fargs=(data, scatters), interval=50, blit=False, repeat=True)

plt.show()




 

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.animation as animation
rc('animation', html='jshtml')
def skel_animation(T):
  global j
  j=0
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

  fig = plt.figure()
  ax = plt.axes(projection='3d')
  
  def skel_vis(_):
    global j
    X = T[j*20:j*20+20, :]
    j+=1
    ax.clear()
    ax.set_title('3D Skeleton')
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)
    
    plot = ax.scatter3D(X[:,0], X[:,2], X[:,1], zdir='z', c= 'red');

    for i in range(nui_skeleton_conn.size//2):
        prva = nui_skeleton_conn[i, 0];
        druga = nui_skeleton_conn[i, 1];
    
        ax.plot([X[prva , 0], X[druga , 0]], [X[ prva, 2], X[druga, 2 ]],zs=[X[prva, 1], X[druga, 1]])
    
    return plot

  return animation.FuncAnimation(fig, skel_vis, frames=63, blit=False, repeat=False)

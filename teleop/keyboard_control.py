import getch
import rospy

from geometry_msgs.msg import Twist


def keys():
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    rospy.init_node('keyboard_control',anonymous=True)
    rate = rospy.Rate(100)
    V = 0.3 #Velocity
    O = 0.3 #Omega
    twist = Twist()
    while not rospy.is_shutdown():
        k=ord(getch.getch())
        if k==119: #W
            print('W, Velocity = {}'.format(V))
            twist.linear.x = V
        elif k==97: #A
            print('A, Omega = {}'.format(O))
            twist.angular.z = O
        elif k==115: #S
            print('S, Velocity = {}'.format(V))
            twist.linear.x = -V
        elif k==100: #D
            print('D, Omega = {}'.format(O))
            twist.angular.z = -O
        elif k==32: #Spacebar
            print('Spacebar, Stopped')
            twist.linear.x = 0
            twist.angular.z = 0
        elif k==103: #G
            print('G, Velocity, Omega = {}, {}'.format(V,O))
            V+=0.1
            O+=0.1
        elif k==98: #B
            if V>=0.2 and O>=0.2:
                V-=0.1
                O-=0.1
            else:
                pass
            print('B, Velocity, Omega = {}, {}'.format(V,O))
        pub.publish(twist)
        rate.sleep()

if __name__=='__main__':
    try:
        keys()
    except rospy.ROSInterruptException:
        pass
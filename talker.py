from std_msgs.msg import String
import rospy
import subprocess
import time



def talker():
    time.sleep(0.1)

    pub = rospy.Publisher('chatter', String, queue_size=20)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i=0

    while(i<10):

        hello_str="hello world %s " % rospy.get_time() 
        pub.publish(hello_str)
        i= i+1


    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

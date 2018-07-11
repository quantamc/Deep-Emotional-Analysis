import rospy
from std_msgs.msg import UInt32
from std_msgs.msg import Header
from std_msgs.msg import Int32
from static_bot_control.msg import EmoMSG
from pprint import pprint
import pickle


def callback(data):
    rospy.loginfo("iiiiii")


def listener():
    rospy.init_node('predictor')

    rospy.Subscriber("frames", EmoMSG, callback)

    rospy.spin()


if __name__ == '__main__':


    # load prediction model from file

    plk_filename = "pickle_model.pk1"
    with open(plk_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    listener()

    WalkPredict = pickle_model.predit()
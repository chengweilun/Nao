# Choregraphe bezier export in Python.
from naoqi import ALProxy
def grab(IP,PORT):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.00302602, [3, -0.733333, 0], [3, 0.733333, 0]], [0.00302602, [3, -0.733333, 0], [3, 0.533333, 0]], [0.00302602, [3, -0.533333, 0], [3, 0.333333, 0]], [0.00449183, [3, -0.333333, 0], [3, 0.533333, 0]], [0.00149202, [3, -0.533333, 0], [3, 0.466667, 0]], [0.00609397, [3, -0.466667, 0], [3, 0.6, 0]], [0.00609397, [3, -0.6, 0], [3, 0.533333, 0]], [0.00149202, [3, -0.533333, 0], [3, 0.6, 0]], [0.00302602, [3, -0.6, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.00302602, [3, -0.733333, 0], [3, 0.733333, 0]], [0.00302602, [3, -0.733333, 0], [3, 0.533333, 0]], [0.00302602, [3, -0.533333, 0], [3, 0.333333, 0]], [0.00709235, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.00310993, [3, -0.533333, 0], [3, 0.466667, 0]], [0.00149202, [3, -0.466667, 0], [3, 0.6, 0]], [0.00149202, [3, -0.6, 0], [3, 0.533333, 0]], [0.00149202, [3, -0.533333, 0], [3, 0.6, 0]], [0.00302602, [3, -0.6, 0], [3, 0.333333, 0]], [0.00149202, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.34826, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.34826, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.34826, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.34826, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.352862, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.34826, [3, -0.466667, 0], [3, 0.6, 0]], [-0.34826, [3, -0.6, 0], [3, 0.533333, 0]], [-0.351328, [3, -0.533333, 0], [3, 0.6, 0]], [-0.34826, [3, -0.6, -0.00306829], [3, 0.333333, 0.00170461]], [0.0996681, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.00464392, [3, -0.733333, 0], [3, 0.733333, 0]], [0.00464392, [3, -0.733333, 0], [3, 0.533333, 0]], [0.00464392, [3, -0.533333, 0], [3, 0.333333, 0]], [0.0135159, [3, -0.333333, 0], [3, 0.533333, 0]], [0.0123138, [3, -0.533333, 0.000759117], [3, 0.466667, -0.000664228]], [0.00924586, [3, -0.466667, 0], [3, 0.6, 0]], [0.00924586, [3, -0.6, 0], [3, 0.533333, 0]], [0.00924586, [3, -0.533333, 0], [3, 0.6, 0]], [0.00464392, [3, -0.6, 0.00460194], [3, 0.333333, -0.00255664]], [-0.122678, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.0551819, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.0413762, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.0413762, [3, -0.533333, 0], [3, 0.333333, 0]], [-1.52856, [3, -0.333333, 0], [3, 0.533333, 0]], [-1.50941, [3, -0.533333, -0.0191488], [3, 0.466667, 0.0167552]], [-1.32533, [3, -0.466667, 0], [3, 0.6, 0]], [-1.32533, [3, -0.6, 0], [3, 0.533333, 0]], [-0.049046, [3, -0.533333, 0], [3, 0.6, 0]], [-0.0551819, [3, -0.6, 0.00613588], [3, 0.333333, -0.00340882]], [-0.421808, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-1.39445, [3, -0.733333, 0], [3, 0.733333, 0]], [-2.06635, [3, -0.733333, 0], [3, 0.533333, 0]], [-1.16435, [3, -0.533333, -0.330683], [3, 0.333333, 0.206677]], [-0.454269, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.460242, [3, -0.533333, 0.00160725], [3, 0.466667, -0.00140635]], [-0.46331, [3, -0.466667, 0], [3, 0.6, 0]], [-0.46331, [3, -0.6, 0], [3, 0.533333, 0]], [-0.477115, [3, -0.533333, 0.0138056], [3, 0.6, -0.0155313]], [-1.39445, [3, -0.6, 0], [3, 0.333333, 0]], [-1.21037, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.0252, [3, -0.733333, 0], [3, 0.733333, 0]], [0.0252, [3, -0.733333, 0], [3, 0.533333, 0]], [0.83, [3, -0.533333, -0.199959], [3, 0.333333, 0.124974]], [1, [3, -0.333333, 0], [3, 0.533333, 0]], [0.2052, [3, -0.533333, 0], [3, 0.466667, 0]], [0.3032, [3, -0.466667, 0], [3, 0.6, 0]], [0.3032, [3, -0.6, 0], [3, 0.533333, 0]], [0.3, [3, -0.533333, 0.00319999], [3, 0.6, -0.00359999]], [0.0252, [3, -0.6, 0], [3, 0.333333, 0]], [0.2876, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.443284, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.443284, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.443284, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.443518, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.443284, [3, -0.533333, -7.60903e-08], [3, 0.466667, 6.6579e-08]], [-0.443284, [3, -0.466667, 0], [3, 0.6, 0]], [-0.443284, [3, -0.6, 0], [3, 0.533333, 0]], [-0.444818, [3, -0.533333, 0], [3, 0.6, 0]], [-0.443284, [3, -0.6, -0.00153415], [3, 0.333333, 0.000852304]], [0.136568, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.00149202, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.00149202, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.00149202, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.00409152, [3, -0.333333, 0.000983324], [3, 0.533333, -0.00157332]], [-0.00916195, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.00455999, [3, -0.466667, 0], [3, 0.6, 0]], [-0.00455999, [3, -0.6, 0], [3, 0.533333, 0]], [0.00464392, [3, -0.533333, 0], [3, 0.6, 0]], [-0.00149202, [3, -0.6, 0], [3, 0.333333, 0]], [0.093616, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[4.19617e-05, [3, -0.733333, 0], [3, 0.733333, 0]], [4.19617e-05, [3, -0.733333, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.00335875, [3, -0.333333, 0.000786659], [3, 0.533333, -0.00125865]], [-0.00609398, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.00302602, [3, -0.466667, 0], [3, 0.6, 0]], [-0.00302602, [3, -0.6, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.6, 0]], [4.19617e-05, [3, -0.6, 0], [3, 0.333333, 0]], [-0.159494, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.691793, [3, -0.733333, 0], [3, 0.733333, 0]], [0.691793, [3, -0.733333, 0], [3, 0.533333, 0]], [0.691793, [3, -0.533333, 0], [3, 0.333333, 0]], [0.692964, [3, -0.333333, 0], [3, 0.533333, 0]], [0.691792, [3, -0.533333, 0], [3, 0.466667, 0]], [0.694859, [3, -0.466667, 0], [3, 0.6, 0]], [0.694859, [3, -0.6, 0], [3, 0.533333, 0]], [0.694859, [3, -0.533333, 0], [3, 0.6, 0]], [0.691793, [3, -0.6, 0.00306656], [3, 0.333333, -0.00170365]], [-0.0859461, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[1.41277, [3, -0.733333, 0], [3, 0.733333, 0]], [1.41277, [3, -0.733333, 0], [3, 0.533333, 0]], [0.174835, [3, -0.533333, 0], [3, 0.333333, 0]], [0.191641, [3, -0.333333, -0.0102266], [3, 0.533333, 0.0163625]], [0.254602, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.254818, [3, -0.466667, 0], [3, 0.6, 0]], [-0.254818, [3, -0.6, 0], [3, 0.533333, 0]], [0.249999, [3, -0.533333, -0.261583], [3, 0.6, 0.294281]], [1.41277, [3, -0.6, -0.0966418], [3, 0.333333, 0.0536899]], [1.46646, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[1.23943, [3, -0.733333, 0], [3, 0.733333, 0]], [1.23943, [3, -0.733333, 0], [3, 0.533333, 0]], [0.644238, [3, -0.533333, 0.233835], [3, 0.333333, -0.146147]], [0.0994838, [3, -0.333333, 0], [3, 0.533333, 0]], [0.151824, [3, -0.533333, -0.0289402], [3, 0.466667, 0.0253227]], [0.262272, [3, -0.466667, -0.110448], [3, 0.6, 0.142005]], [1.32645, [3, -0.6, 0], [3, 0.533333, 0]], [1.24557, [3, -0.533333, 0.00545475], [3, 0.6, -0.00613659]], [1.23943, [3, -0.6, 0.00613659], [3, 0.333333, -0.00340922]], [0.164096, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.00157595, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.823801, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.813062, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.85234, [3, -0.333333, 0.00325484], [3, 0.533333, -0.00520774]], [-0.857548, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.842994, [3, -0.466667, 0], [3, 0.6, 0]], [-0.842994, [3, -0.6, 0], [3, 0.533333, 0]], [-0.848343, [3, -0.533333, 0], [3, 0.6, 0]], [-0.00157595, [3, -0.6, -0.151866], [3, 0.333333, 0.0843698]], [0.0827939, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.358915, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.358915, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.358915, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.358915, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.360448, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.357381, [3, -0.466667, 0], [3, 0.6, 0]], [-0.357381, [3, -0.6, 0], [3, 0.533333, 0]], [-0.363515, [3, -0.533333, 0], [3, 0.6, 0]], [-0.358915, [3, -0.6, -0.00460068], [3, 0.333333, 0.00255593]], [0.0874801, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.00916195, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.00916195, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.00916195, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.0178491, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.0106959, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.0122299, [3, -0.466667, 0], [3, 0.6, 0]], [-0.0122299, [3, -0.6, 0], [3, 0.533333, 0]], [-0.0152981, [3, -0.533333, 0], [3, 0.6, 0]], [-0.00916195, [3, -0.6, -0.00613618], [3, 0.333333, 0.00340899]], [0.121228, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.0567998, [3, -0.733333, 0], [3, 0.733333, 0]], [0.0445281, [3, -0.733333, 0], [3, 0.533333, 0]], [0.0445281, [3, -0.533333, 0], [3, 0.333333, 0]], [1.4591, [3, -0.333333, 0], [3, 0.533333, 0]], [1.40519, [3, -0.533333, 0.0254011], [3, 0.466667, -0.022226]], [1.31621, [3, -0.466667, 0], [3, 0.6, 0]], [1.31621, [3, -0.6, 0], [3, 0.533333, 0]], [0.046062, [3, -0.533333, 0], [3, 0.6, 0]], [0.0567998, [3, -0.6, -0.0107378], [3, 0.333333, 0.00596544]], [0.42496, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[1.3959, [3, -0.733333, 0], [3, 0.733333, 0]], [2.0678, [3, -0.733333, 0], [3, 0.533333, 0]], [1.16733, [3, -0.533333, 0.324938], [3, 0.333333, -0.203086]], [0.483725, [3, -0.333333, 0.00418316], [3, 0.533333, -0.00669306]], [0.477032, [3, -0.533333, 0], [3, 0.466667, 0]], [0.496974, [3, -0.466667, 0], [3, 0.6, 0]], [0.496974, [3, -0.6, 0], [3, 0.533333, 0]], [0.486237, [3, -0.533333, 0], [3, 0.6, 0]], [1.3959, [3, -0.6, 0], [3, 0.333333, 0]], [1.21182, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.0192, [3, -0.733333, 0], [3, 0.733333, 0]], [0.0192, [3, -0.733333, 0], [3, 0.533333, 0]], [0.83, [3, -0.533333, -0.20119], [3, 0.333333, 0.125744]], [1, [3, -0.333333, 0], [3, 0.533333, 0]], [0.116, [3, -0.533333, 0], [3, 0.466667, 0]], [0.304, [3, -0.466667, 0], [3, 0.6, 0]], [0.304, [3, -0.6, 0], [3, 0.533333, 0]], [0.3, [3, -0.533333, 0.00399998], [3, 0.6, -0.00449998]], [0.0192, [3, -0.6, 0], [3, 0.333333, 0]], [0.2852, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-0.44797, [3, -0.733333, 0], [3, 0.733333, 0]], [-0.44797, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.44797, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.448208, [3, -0.333333, 0.000237388], [3, 0.533333, -0.00037982]], [-0.454106, [3, -0.533333, 0.00159391], [3, 0.466667, -0.00139467]], [-0.457173, [3, -0.466667, 0], [3, 0.6, 0]], [-0.457173, [3, -0.6, 0], [3, 0.533333, 0]], [-0.454105, [3, -0.533333, -0.00144363], [3, 0.6, 0.00162408]], [-0.44797, [3, -0.6, -0.00613482], [3, 0.333333, 0.00340824]], [0.141086, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[4.19617e-05, [3, -0.733333, 0], [3, 0.733333, 0]], [4.19617e-05, [3, -0.733333, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [0.00872912, [3, -0.333333, 0], [3, 0.533333, 0]], [0.0061779, [3, -0.533333, 0], [3, 0.466667, 0]], [0.00617791, [3, -0.466667, 0], [3, 0.6, 0]], [0.00617791, [3, -0.6, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.6, 0]], [4.19617e-05, [3, -0.6, 0], [3, 0.333333, 0]], [-0.091998, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[4.19617e-05, [3, -0.733333, 0], [3, 0.733333, 0]], [4.19617e-05, [3, -0.733333, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.333333, 0]], [-0.00335875, [3, -0.333333, 0.000786659], [3, 0.533333, -0.00125865]], [-0.00609398, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.00302602, [3, -0.466667, 0], [3, 0.6, 0]], [-0.00302602, [3, -0.6, 0], [3, 0.533333, 0]], [4.19617e-05, [3, -0.533333, 0], [3, 0.6, 0]], [4.19617e-05, [3, -0.6, 0], [3, 0.333333, 0]], [-0.159494, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.693411, [3, -0.733333, 0], [3, 0.733333, 0]], [0.693411, [3, -0.733333, 0], [3, 0.533333, 0]], [0.693411, [3, -0.533333, 0], [3, 0.333333, 0]], [0.694576, [3, -0.333333, 0], [3, 0.533333, 0]], [0.690342, [3, -0.533333, 0.00184369], [3, 0.466667, -0.00161323]], [0.684206, [3, -0.466667, 0], [3, 0.6, 0]], [0.684206, [3, -0.6, 0], [3, 0.533333, 0]], [0.693411, [3, -0.533333, 0], [3, 0.6, 0]], [0.693411, [3, -0.6, 0], [3, 0.333333, 0]], [-0.0889301, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[1.43893, [3, -0.733333, 0], [3, 0.733333, 0]], [1.43893, [3, -0.733333, 0], [3, 0.533333, 0]], [0.173384, [3, -0.533333, 0], [3, 0.333333, 0]], [0.284489, [3, -0.333333, -0.0198633], [3, 0.533333, 0.0317813]], [0.328318, [3, -0.533333, 0], [3, 0.466667, 0]], [-0.254818, [3, -0.466667, 0], [3, 0.6, 0]], [-0.254818, [3, -0.6, 0], [3, 0.533333, 0]], [0.227074, [3, -0.533333, -0.265686], [3, 0.6, 0.298897]], [1.43893, [3, -0.6, -0.0276145], [3, 0.333333, 0.0153414]], [1.45427, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[-1.24258, [3, -0.733333, 0], [3, 0.733333, 0]], [-1.24258, [3, -0.733333, 0], [3, 0.533333, 0]], [-0.644321, [3, -0.533333, -0.224099], [3, 0.333333, 0.140062]], [-0.150098, [3, -0.333333, 0], [3, 0.533333, 0]], [-0.227074, [3, -0.533333, 0.0207752], [3, 0.466667, -0.0181783]], [-0.266959, [3, -0.466667, 0.0398847], [3, 0.6, -0.0512803]], [-1.32645, [3, -0.6, 0], [3, 0.533333, 0]], [-1.24872, [3, -0.533333, -0.00545475], [3, 0.6, 0.00613659]], [-1.24258, [3, -0.6, -0.00613659], [3, 0.333333, 0.00340922]], [-0.17185, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([2.2, 4.4, 6, 7, 8.6, 10, 11.8, 13.4, 15.2, 16.2])
    keys.append([[0.00916195, [3, -0.733333, 0], [3, 0.733333, 0]], [0.845191, [3, -0.733333, 0], [3, 0.533333, 0]], [0.834454, [3, -0.533333, 0], [3, 0.333333, 0]], [0.87996, [3, -0.333333, 0], [3, 0.533333, 0]], [0.865134, [3, -0.533333, 0.00345373], [3, 0.466667, -0.00302201]], [0.860533, [3, -0.466667, 0], [3, 0.6, 0]], [0.860533, [3, -0.6, 0], [3, 0.533333, 0]], [0.882007, [3, -0.533333, 0], [3, 0.6, 0]], [0.00916195, [3, -0.6, 0], [3, 0.333333, 0]], [0.0689882, [3, -0.333333, 0], [3, 0, 0]]])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", IP, 9559)
      motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
      print err




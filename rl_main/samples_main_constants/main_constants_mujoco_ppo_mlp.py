from rl_main.conf.constants_general import *
from rl_main.conf.names import *

# [GENERAL]
SEED = 1
MY_PLATFORM = OSName.MAC
PYTHON_PATH = "~/anaconda3/envs/rl/bin/python"
ENV_RENDER = False

# [MQTT]
MQTT_SERVER = "localhost"
MQTT_PORT = 1883
MQTT_LOG = False

# [WORKER]
NUM_WORKERS = 1

# [OPTIMIZATION]
MAX_EPISODES = 5000
GAMMA = 0.98
#GAMMA = 1.0

# [MODE]
MODE_SYNCHRONIZATION = True
MODE_GRADIENTS_UPDATE = True      # Distributed
MODE_PARAMETERS_TRANSFER = True    # Transfer

# [TRAINING]
OPTIMIZER = OptimizerName.ADAM
GAE_LAMBDA = 0.99
LEARNING_RATE = 0.0001

# [TRAJECTORY_SAMPLING]
TRAJECTORY_SAMPLING = True
TRAJECTORY_LIMIT_SIZE = 500
TRAJECTORY_BATCH_SIZE = 20

# [PPO]
PPO_K_EPOCH = 500
PPO_EPSILON_CLIP = 0.2
PPO_VALUE_LOSS_WEIGHT = 0.5
PPO_ENTROPY_WEIGHT = 0.01

# [1. ENVIRONMENTS]
# ENVIRONMENT_ID = EnvironmentName.INVERTED_DOUBLE_PENDULUM_V2
ENVIRONMENT_ID = EnvironmentName.INVERTED_PENDULUM_V2
# ENVIRONMENT_ID = EnvironmentName.HOPPER_V2
# ENVIRONMENT_ID = EnvironmentName.ANT_V2
# ENVIRONMENT_ID = EnvironmentName.HALF_CHEETAH_V2
# ENVIRONMENT_ID = EnvironmentName.SWIMMER_V2
# ENVIRONMENT_ID = EnvironmentName.REACHER_V2
# ENVIRONMENT_ID = EnvironmentName.HUMANOID_V2
# ENVIRONMENT_ID = EnvironmentName.HUMANOID_STAND_UP_V2
# ENVIRONMENT_ID = EnvironmentName.WALKER_2D_V2

# [2. DEEP_LEARNING_MODELS]
DEEP_LEARNING_MODEL = DeepLearningModelName.ActorCriticMLP
# DEEP_LEARNING_MODEL = DeepLearningModelName.ActorCriticCNN
# DEEP_LEARNING_MODEL = DeepLearningModelName.NoModel

# [3. ALGORITHMS]
# RL_ALGORITHM = RLAlgorithmName.DQN_V0
RL_ALGORITHM = RLAlgorithmName.PPO_V0
# RL_ALGORITHM = RLAlgorithmName.Monte_Carlo_Control_V0
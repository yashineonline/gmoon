# Humanoid RL Project

## Overview

Minimal scaffold combining Isaac Gym simulation, PyTorch deep RL (PPO), and ROS2 control bridge for a humanoid prototype.

---

### Directory Tree

```
humanoid-rl-research/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
│
├── src/
│   ├── irreversible_rl_simulations.py  # All simulations
│   ├── agent_utils.py                  # Optional modular helpers
│   ├── config.yaml                     # Configs if used
│
├── notebooks/
│   └── results_analysis.ipynb          # Plots, analysis
│
├── results/
│   └── minigrid/
│   └── mujoco/
│   └── isaac/
│
└── gifs/
    └── demo.gif
```


---

```
humanoid_rl/
├── README.md
├── requirements.txt
├── ros2_ws/
│   ├── src/
│   │   └── humanoid_control/
│   │       ├── package.xml
│   │       ├── setup.py
│   │       └── humanoid_control/
│   │           ├── __init__.py
│   │           └── control_node.py
└── python/
    ├── envs/
    │   └── humanoid_env.py
    └── train_policy.py
```

---

### requirements.txt

```text
isaacgym==0.2.3
torch>=2.1
stable-baselines3==2.3.0
gym==0.26
rclpy
numpy
```

---

### README.md (excerpt)

```markdown
# Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Build ROS2 workspace
cd ros2_ws && colcon build
source install/setup.bash
```

---

### python/envs/humanoid\_env.py (simplified)

```python
import torch
from isaacgym import gymapi
from isaacgym import gymtorch
import gym
from gym import spaces

class HumanoidEnv(gym.Env):
    def __init__(self, cfg):
        self.gym = gymapi.acquire_gym()
        # create sim, load asset, etc.
        # ...
        self.obs_space = spaces.Box(-1.0, 1.0, (cfg['obs_dim'],), dtype=float)
        self.act_space = spaces.Box(-1.0, 1.0, (cfg['act_dim'],), dtype=float)

    def step(self, action):
        # apply forces to humanoid joints
        # ...
        reward = self.compute_reward()
        done = self.check_terminate()
        return self.get_obs(), reward, done, {}

    def reset(self):
        # reset sim
        # ...
        return self.get_obs()

    def get_obs(self):
        # return concatenated joint angles, velocities, root pose
        return self.obs_buf
```

---

### python/train\_policy.py (simplified)

```python
import torch
from stable_baselines3 import PPO
from envs.humanoid_env import HumanoidEnv

cfg = dict(obs_dim=120, act_dim=28)
env = HumanoidEnv(cfg)
model = PPO("MlpPolicy", env, verbose=1, n_steps=2048, batch_size=512,
            tensorboard_log="./tb")

model.learn(total_timesteps=3_000_000)
model.save("ppo_humanoid")
```

---

### ros2\_ws/src/humanoid\_control/control\_node.py

```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import torch

class HumanoidControl(Node):
    def __init__(self):
        super().__init__('humanoid_control')
        self.pub = self.create_publisher(JointState, '/humanoid/joint_cmd', 10)
        self.model = torch.jit.load('ppo_humanoid.pt')
        self.create_timer(0.02, self.control_callback)  # 50 Hz

    def control_callback(self):
        # TODO: subscribe to /humanoid/joint_states and sensor topics
        obs = self.get_obs()
        action, _ = self.model.predict(obs, deterministic=False)
        msg = JointState()
        msg.position = action.tolist()
        self.pub.publish(msg)

    def get_obs(self):
        # TODO: assemble observation vector from sensors
        return []


def main():
    rclpy.init()
    node = HumanoidControl()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
```

---

## Quick Run

1. **Train in simulation**

   ```bash
   python python/train_policy.py
   ```
2. **Launch ROS2 control node**

   ```bash
   source ros2_ws/install/setup.bash
   ros2 run humanoid_control control_node
   ```

---

## Skill Tests

* **Adaptability:** Randomize terrain in env and retrain.
* **Fail‑safe:** Disable one joint mid‑episode, maintain balance.
* **Latency:** Measure ROS2 round‑trip latencies (goal <20 ms).

# hello-wandb

### WandB Demo Scripts

This repository contains two Python scripts that demonstrate how to use [Weights & Biases (W&B)](https://wandb.ai) for tracking and visualizing machine learning experiments.

#### **Scripts Included**
1. **`hello-wandb.py`**:
   - A beginner-friendly script (provided by wandb.ai) showcasing basic W&B functionalities.
   - Logs simple training metrics (`accuracy` and `loss`) for a simulated training loop.

2. **`advanced-wandb-demo.py`**:
   - A more advanced script demonstrating additional W&B features:
     - Logs both training and validation metrics.
     - Tracks hyperparameters like learning rate and architecture.
     - Saves and uploads a dummy model file.

#### **Setup**
1. **Install W&B**:

   ```sh
   pip install wandb
   ```

2. **Log In**:
   - Run `wandb login` and authenticate using the provided link.

#### **How to Run**
1. Run the beginner script:

   ```sh
   python hello-wandb.py
   ```

   - Logs metrics to the project `my-awesome-project`.

2. Run the advanced script:

   ```sh
   python advanced-wandb-demo.py
   ```

   - Logs metrics and files to the project `advanced-wandb-demo`.

#### **View Results**
- Visit [W&B](https://wandb.ai) and navigate to the respective projects (`my-awesome-project` or `advanced-wandb-demo`) to view dashboards with logged metrics and configurations. 

---

My projects:

https://wandb.ai/tdiprima/my-awesome-project

https://wandb.ai/tdiprima/advanced-wandb-demo

<br>

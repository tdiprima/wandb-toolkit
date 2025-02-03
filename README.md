# wandb-toolkit

### WandB Demo Scripts

This repository contains Python scripts that demonstrate how to use [Weights & Biases (W&B)](https://wandb.ai) for tracking and visualizing machine learning experiments.

#### **Scripts Included**
1. **`hello-wandb.py`**:
   - A beginner-friendly script (provided by wandb.ai) showcasing basic W&B functionalities.
   - Logs simple training metrics (`accuracy` and `loss`) for a simulated training loop.

2. **`advanced-wandb-demo.py`**:
   - A more advanced script demonstrating additional W&B features:
     - Logs both training and validation metrics.
     - Tracks hyperparameters like learning rate and architecture.
     - Saves and uploads a dummy model file.

3. **`fruit-extractor-weave.py`**:
   - Combines W&B Weave with the OpenAI API to track and log sentence parsing tasks.
   - Parses sentences into structured JSON objects with keys like `fruit`, `color`, and `flavor`.
   - Demonstrates integration of external APIs and W&B’s function tracking capabilities.

#### **Setup**
1. **Install W&B**:

   ```sh
   pip install wandb weave openai
   ```

2. **Log In**:
   - Run `wandb login` and authenticate using the provided link.

3. **Set OpenAI API Key**:
   - Store your API key as an environment variable:

     ```sh
     export OPENAI_API_KEY=your_api_key_here
     ```

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

3. Run the fruit extraction script:

   ```sh
   python fruit-extractor-weave.py
   ```

   - Tracks sentence parsing tasks and outputs structured JSON.

#### **View Results**
- Visit [W&B](https://wandb.ai) and navigate to the respective projects (`my-awesome-project`, `advanced-wandb-demo`, or `PyTorch Experiments`) to view dashboards with logged metrics and configurations.

### Licensing Notice

This project includes third-party open-source code, which remains subject to its original licenses.  
Attribution is provided in the source code where applicable.  

If you believe there is an issue with licensing, please **open an issue** or **contact the repository owner** for resolution.

<br>

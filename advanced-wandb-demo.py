# This script takes W&B logging a step further, showcasing advanced features like logging multiple metrics, 
# saving and uploading model files, and visualizing hyperparameter sweeps.
import wandb
import random
import math

# Initialize a new W&B run with a different project name
wandb.init(
    project="advanced-wandb-demo",
    config={
        "learning_rate": 0.01,
        "architecture": "ResNet50",
        "dataset": "ImageNet",
        "batch_size": 32,
        "epochs": 20,
    },
)

# Config for easy access
config = wandb.config

# Simulate training for multiple metrics
for epoch in range(1, config.epochs + 1):
    # Calculate a simulated accuracy value based on the logarithmic growth of epochs
    # with some added randomness to make the results more dynamic.
    acc = math.log(epoch + 1) / math.log(config.epochs + 1) + random.uniform(-0.01, 0.01)

    # Simulate validation accuracy slightly lower than training accuracy
    # by subtracting a small random value.
    val_acc = acc - random.uniform(0.01, 0.03)

    # Simulate a training loss that decreases exponentially as epochs progress,
    # with some randomness to make it more realistic.
    loss = math.exp(-epoch / config.epochs) + random.uniform(-0.01, 0.01)

    # Simulate validation loss slightly higher than training loss
    # by adding a small random value.
    val_loss = loss + random.uniform(0.01, 0.02)

    # Log metrics
    wandb.log({
        "epoch": epoch,
        "accuracy": acc,
        "val_accuracy": val_acc,
        "loss": loss,
        "val_loss": val_loss,
    })

    # Example of logging a model file
    if epoch == config.epochs:
        with open("dummy_model.h5", "w") as f:
            f.write("This is a dummy model file for W&B demo.")
        wandb.save("dummy_model.h5")

# Finish the W&B run
wandb.finish()

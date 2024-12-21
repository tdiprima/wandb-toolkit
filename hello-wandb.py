# From "PyTorch Experiments" script in wandb.ai
import wandb
import random

# start a new wandb run to track this script
wandb.init(
    # set the wandb project where this run will be logged
    project="my-awesome-project",
    
    # track hyperparameters and run metadata
    config={
    "learning_rate": 0.02,
    "architecture": "CNN",
    "dataset": "CIFAR-100",
    "epochs": 10,
    }
)

# simulate training
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    # Calculate a simulated accuracy that starts low and gradually approaches 1 (perfect accuracy)
    # as the epochs increase. Random noise and an offset are subtracted to make it less uniform.
    acc = 1 - 2 ** -epoch - random.random() / epoch - offset

    # Calculate a simulated loss that starts high and decreases exponentially as the epochs increase.
    # Random noise and an offset are added to make the values appear more dynamic and realistic.
    loss = 2 ** -epoch + random.random() / epoch + offset

    # log metrics to wandb
    wandb.log({"acc": acc, "loss": loss})
    
# [optional] finish the wandb run, necessary in notebooks
wandb.finish()

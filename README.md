# mppi_rollouts
ROS Noetic package that calculates MPPI rollout trajectories using trained function encoders.

## Updates for _Zero to Autonomy in Real-Time: Online Adaptation of Dynamics in Unstructured Environments_
Our new paper introduced recursive least squares updates to function encoder models that adapts
the model's coefficients to new terrains in real time using streaming odometry data.

In the paper's simulation experiments, we used
-   `rls_experiments.launch` to run the RLS adaptation model.
-   `maml_experiments.launch` to run a baseline MAML model for comparison.
-   `rollouts_server_fe_node.py` to run baseline, static FE and NODE models for comparison.

For this paper, we updated our Unity simulation to allow dynamic terrain changes, triggered
by a ROS topic command (see `trigger_changer*.py`). 

Additionally, we deployed our trained models on Clearpath Jackal (see the `jackal_experiments` branch). 

All models evaluated for this paper were trained using the [terrain-adaptation-rls](https://github.com/willward20/terrain-adaptation-rls) repository. 

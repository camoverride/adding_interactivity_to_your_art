# Adding Interactivity to Your Art


## Materials

Find documents and slides [here](https://drive.google.com/drive/folders/1vVtPyT6_q_rB5KtS1h_qkVjmQtyO_W2H?usp=drive_link).


## Getting Started

- Fork this repo

- Clone your fork:
`git clone git@github.com:<your_username>/adding_interactivity_to_your_art.git`

- Navigate to the repo:
`cd adding_interactivity_to_your_art`

- Create a virtual environment:
`python3 -m venv .venv`

- Activate the virtual environment:
`source .venv/bin/activate`

- Install the requirements:
`pip install -r requirements.txt`


## Test the Program

- `python hand_tracking.py`


## Run in Production

Start a service with `systemd`. This will start the program when the computer starts and revive it when it dies. It expects that the directory is `/home/pi/adding_interactivity_to_your_art`:
- `mkdir -p ~/.config/systemd/user`
 - `cat tracking.service > ~/.config/systemd/user/tracking.service`

Start the service using the commands below:
- `systemctl --user daemon-reload`
- `systemctl --user enable tracking.service`
- `systemctl --user start tracking.service`

Start it on boot:
- `sudo loginctl enable-linger pi`

Get the status:
- `systemctl --user status tracking.service`

Get the logs:
- `journalctl --user -u telephone.service`

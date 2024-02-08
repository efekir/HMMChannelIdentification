import random
import matplotlib.pyplot as plt

class HMMChannelIdentification:
    def _init_(self, num_channels, num_iterations):
        self.num_channels = num_channels
        self.num_iterations = num_iterations
        self.occupied_probability = 0.2  # Probability of a channel being occupied
        self.transition_matrix = [[random.random() for _ in range(num_channels)] for _ in range(num_channels)]
        self.emission_matrix = [[random.random() for _ in range(num_channels)] for _ in range(num_channels)]
        self.initial_state_probabilities = [random.random() for _ in range(num_channels)]

    def simulate(self):
        vacant_channels = 0
        for _ in range(self.num_iterations):
            # Simulate HMM algorithm
            sensed_channels = self.sense_channels()
            vacant_channels += sensed_channels.count(0)

        return vacant_channels

    def sense_channels(self):
        # Simulate sensing the channels based on the HMM model
        current_state = random.choice(range(self.num_channels))
        sensed_channels = [0] * self.num_channels

        for i in range(self.num_channels):
            sensed_channels[i] = 0 if random.random() < self.emission_matrix[current_state][i] else 1

        return sensed_channels

class CRAlgorithm:
    def _init_(self, num_channels, num_packets):
        self.num_channels = num_channels
        self.num_packets = num_packets
        self.channel_busy_probability = 0.5  # Probability of the channel being busy

    def simulate(self):
        vacant_channels = 0
        for _ in range(self.num_packets):
            # Simulate CRAlgorithm
            if self.is_channel_busy():
                self.wait_and_sense_again()
            else:
                vacant_channels += 1
                self.send_beacon_to_iot_devices()

        return vacant_channels

    def is_channel_busy(self):
        # Simulate sensing the channel
        return random.random() < self.channel_busy_probability

    def wait_and_sense_again(self):
        # Simulate waiting for a random time before sensing again
        wait_time = random.uniform(0.5, 1.5)
        print(f"Waiting for {wait_time:.2f} seconds...")
        # Simulate sensing the channel again after waiting
        if self.is_channel_busy():
            self.stop_communication()
        else:
            print("Channel is not busy now. Resuming communication.")

    def send_beacon_to_iot_devices(self):
        # Simulate sending a beacon to IoT devices
        print("Sending beacon to IoT devices...")

    def stop_communication(self):
        # Simulate stopping communication due to a busy channel
        print("Communication stopped due to a busy channel.")

# Function to simulate the algorithms and collect results
def simulate_algorithms(num_channels, num_packets, num_iterations):
    hmm_simulator = HMMChannelIdentification(num_channels=num_channels, num_iterations=num_iterations)
    hmm_result = hmm_simulator.simulate()

    cr_simulator = CRAlgorithm(num_channels=num_channels, num_packets=num_packets)
    cr_result = cr_simulator.simulate()

    random_result = random.randint(0, num_iterations)  # Randomly generate a result for comparison

    return hmm_result, cr_result, random_result

# Simulate with larger sample size and delays
num_channels = 10
num_packets = 1000
num_iterations = 1000

hmm_results = []
cr_results = []
random_results = []

for _ in range(10):  # Repeat the simulation for more reliable results
    hmm_result, cr_result, random_result = simulate_algorithms(num_channels, num_packets, num_iterations)
    hmm_results.append(hmm_result)
    cr_results.append(cr_result)
    random_results.append(random_result)

# Plot the results with delays
plt.figure(figsize=(10, 6))

plt.plot(hmm_results, label='HMM with Delays', linestyle='dashed', marker='o')
plt.plot(cr_results, label='CRAlgorithm with Delays', linestyle='dashed', marker='o')
plt.plot(random_results, label='Random with Delays', linestyle='dashed', marker='o')

plt.title('Comparison of Vacant Channel Identification Algorithms with Delays')
plt.xlabel('Simulation Iteration')
plt.ylabel('Number of Vacant Channels')
plt.legend()
plt.show()
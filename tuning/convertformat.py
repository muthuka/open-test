# Modify a josnl file to a format that can be used by the tuning program
# The input file is a jsonl file with the following format:
# {"source": "Dove_final", "conversation": [{"input": "explain Tuckman's stages of group development", "output": "Tuckman's stages of group development is a widely accepted model that describes the typical progression of a group's behavior and interactions as it evolves over time. Developed by psychologist Bruce Tuckman in 1965, the model originally consisted of four stages, with a fifth stage added in 1977. The five stages are:\n\n1. Forming: This is the initial stage, where group members come together and begin to get to know each other. At this stage, individuals tend to be polite and cautious, as they try to understand the group's purpose, establish relationships, and determine their roles within the group. There may be a reliance on the group leader for guidance and direction.\n2. Storming: As group members become more comfortable, they may start to express differing opinions, challenge each other, and engage in conflicts. This stage is characterized by a struggle for power and control, as individuals vie for positions and roles within the group. The storming stage can be stressful and uncomfortable, but it's a necessary part of the group's development as they learn to navigate differences and establish norms.\n3. Norming: In this stage, the group begins to find its stride as members establish a sense of cohesion and unity. Norms and expectations are clarified, roles solidify, and members start to trust and support one another. Conflict may still arise, but the group is generally better equipped to resolve disputes and work through challenges together.\n4. Performing: At the performing stage, the group is now functioning at a high level of productivity and effectiveness. Members have a clear understanding of their roles, goals, and how to work together. The group is able to make decisions and solve problems efficiently, and members can rely on each other to fulfill their responsibilities. The emphasis shifts from individual needs to collective achievement.\n5. Adjourning (or Mourning): This stage was added later to the model to address the process of a group's dissolution or completion of its purpose. In the adjourning stage, members may experience a range of emotions, from pride in their accomplishments to sadness or anxiety about the group disbanding. This stage is an opportunity for members to reflect on their experiences, celebrate their achievements, and prepare for the transition to new endeavors.\n\nIt's important to note that not all groups progress linearly through these stages. Some groups may skip or repeat stages, or even experience multiple stages simultaneously. Nonetheless, Tuckman's model provides a useful framework for understanding the typical dynamics of group development."}]}
# The output file is a jsonl file with the following format:
# {"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "explain Tuckman's stages of group development"}, {"role": "assistant", "content": "Tuckman's stages of group development is a widely accepted model that describes the typical progression of a group's behavior and interactions as it evolves over time. Developed by psychologist Bruce Tuckman in 1965, the model originally consisted of four stages, with a fifth stage added in 1977. The five stages are:\n\n1. Forming: This is the initial stage, where group members come together and begin to get to know each other. At this stage, individuals tend to be polite and cautious, as they try to understand the group's purpose, establish relationships, and determine their roles within the group. There may be a reliance on the group leader for guidance and direction.\n2. Storming: As group members become more comfortable, they may start to express differing opinions, challenge each other, and engage in conflicts. This stage is characterized by a struggle for power and control, as individuals vie for positions and roles within the group. The storming stage can be stressful and uncomfortable, but it's a necessary part of the group's development as they learn to navigate differences and establish norms.\n3. Norming: In this stage, the group begins to find its stride as members establish a sense of cohesion and unity. Norms and expectations are clarified, roles solidify, and members start to trust and support one another. Conflict may still arise, but the group is generally better equipped to resolve disputes and work through challenges together.\n4. Performing: At the performing stage, the group is now functioning at a high level of productivity and effectiveness. Members have a clear understanding of their roles, goals, and how to work together. The group is able to make decisions and solve problems efficiently, and members can rely on each other to fulfill their responsibilities. The emphasis shifts from individual needs to collective achievement.\n5. Adjourning (or Mourning): This stage was added later to the model to address the process of a group's dissolution or completion of its purpose. In the adjourning stage, members may experience a range of emotions, from pride in their accomplishments to sadness or anxiety about the group disbanding. This stage is an opportunity for members to reflect on their experiences, celebrate their achievements, and prepare for the transition to new endeavors.\n\nIt's important to note that not all groups progress linearly through these stages. Some groups may skip or repeat stages, or even experience multiple stages simultaneously. Nonetheless, Tuckman's model provides a useful framework for understanding the typical dynamics of group development."}]}

import jsonlines
import json
import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        description='Convert jsonl file to a format that can be used by the tuning program')
    parser.add_argument('--input', type=str, help='input file path')
    parser.add_argument('--output', type=str, help='output file path')
    args = parser.parse_args()

    with jsonlines.open(args.input) as reader:
        with jsonlines.open(args.output, mode='w') as writer:
            for obj in reader:
                messages = []

                messages.append(
                    {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."})
                messages.append(
                    {"role": "user", "content": obj["conversation"][0]["input"]})
                messages.append(
                    {"role": "assistant", "content": obj["conversation"][0]["output"]})
                writer.write({"messages": messages})


if __name__ == "__main__":
    main()

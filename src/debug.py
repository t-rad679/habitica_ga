import client.habitica_client as habitica_client


def main():
    response = habitica_client.create_task(habitica_client.TaskType.TODO, "test", habitica_client.Difficulty.TRIVIAL)
    print(response.text)


if __name__ == "__main__":
    main()

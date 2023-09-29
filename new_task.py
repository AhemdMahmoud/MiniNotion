{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 384
        },
        "id": "8fKHAquSnAcq",
        "outputId": "64cf88e7-02e0-47ec-bcc0-52c2ef6869b1"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-bbd1bdadeaa5>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# import task_manager   1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;31m# import task_manager as  tm  2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtask_manager\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mview_tasks\u001b[0m  \u001b[0;31m#or *\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m tasks = [\n\u001b[1;32m      5\u001b[0m     \u001b[0;34m{\u001b[0m\u001b[0;34m\"task\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"Quran\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"completed\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'task_manager'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "# import task_manager   1\n",
        "# import task_manager as  tm  2\n",
        "from task_manager import view_tasks  #or *\n",
        "tasks = [\n",
        "    {\"task\": \"Quran\", \"completed\": True},\n",
        "    {\"task\": \"Salah\", \"completed\": True},\n",
        "    {\"task\": \"Study\", \"completed\": False},\n",
        "    {\"task\": \"Exercise\", \"completed\": True},\n",
        "    {\"task\": \"Sleep\", \"completed\": False},\n",
        "    {\"task\": \"Visit Hamada\", \"completed\": True}\n",
        "]\n",
        "# task_manager.view_tasks(tasks)   1\n",
        "# ts.view_tasks(tasks) 2\n",
        "view_tasks(tasks)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "                      #or use none pythonic code\n",
        " # def view_tasks(tasks_list):\n",
        "#   if tasks_list :\n",
        "\n",
        "#     print(\"All tasks:\")\n",
        "#     for index, task in enumerate(tasks_list, 1):\n",
        "#         status = \"✔\" if task[\"completed\"] else \"🛶\"\n",
        "#         print(f\"{index}. {task['task']} - {status}\")\n",
        "#         print(\"*\"*30)\n",
        "#   else :\n",
        "    # print (\"no tasks to show\")\n",
        "# view_tasks(tasks)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "20LpDdV6osE8"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
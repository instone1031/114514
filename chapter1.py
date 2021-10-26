{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chapter1.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyO3odQsBjBMiLmVTO71veWr",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/instone1031/114514/blob/main/chapter1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gFm6cZMuWbmt"
      },
      "source": [
        "# 연습문제"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q3YczgxwWebt"
      },
      "source": [
        "# 1번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wFSN9G3rWbTf",
        "outputId": "bf8f0b27-b855-48f7-d537-b8b3ac266b36"
      },
      "source": [
        "print(\"환영합니다.\")\n",
        "print(\"파이썬의 세계에 오신 것을 환영합니다.\")\n",
        "print(\"파이썬은 강력합니다.\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "환영합니다.\n",
            "파이썬의 세계에 오신 것을 환영합니다.\n",
            "파이썬은 강력합니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XmAzIv7NWweK"
      },
      "source": [
        "# 2번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y210XLWkWywW",
        "outputId": "36097da5-c93d-4a37-cfe6-a9045e6b6634"
      },
      "source": [
        "print(\"반갑습니다. 파이썬!\")\n",
        "print(2*3/10)\n",
        "print(\"Hello\", \"world\", \"!!!\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "반갑습니다. 파이썬!\n",
            "0.6\n",
            "Hello world !!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EMpwZ5XnXCnk"
      },
      "source": [
        "# 3번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6CdCLoX-XD4Y",
        "outputId": "06e3c367-b84f-445f-913b-d93d5a0036f2"
      },
      "source": [
        "print(7*24)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "168\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d-aQyfCAXXD9"
      },
      "source": [
        "# 4번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kjv9j0F9XYU2"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "\n",
        "t.forward(100)\n",
        "t.left(90)\n",
        "t.forward(100)\n",
        "t.right(90)\n",
        "t.forward(100)\n",
        "t.right(90)\n",
        "t.forward(100)\n",
        "t.left(90)\n",
        "t.forward(100)\n",
        "exitonclick()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IfIvB6noYDhb"
      },
      "source": [
        "# 5번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-4UKSJlpYHup"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "t,width(10)\n",
        "\n",
        "t.forward(100)\n",
        "t.left(90)\n",
        "t.forward(100)\n",
        "t._screen.exitonclick()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "C_Cdq74ZYevM"
      },
      "source": [
        "# 6번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A0_dO1BJYf-D"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "t.color(\"blue\")\n",
        "\n",
        "t.forward(100)\n",
        "t._screen.exitonclick()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9r-yqeSPYx3Z"
      },
      "source": [
        "# 7번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aycWqNPaYzoA"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"square\")\n",
        "\n",
        "t.forward(100)\n",
        "t._screen.exitonclick()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "P6-s0J7TZB5x"
      },
      "source": [
        "# 8번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2tTzB0W4ZDCd"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "\n",
        "t.up()\n",
        "t.goto(0, 0)\n",
        "t.down()\n",
        "t.forward(100);\n",
        "\n",
        "t.up()\n",
        "t.goto(0, 100)\n",
        "t.down()\n",
        "t.forward(100);\n",
        "t._screen.exitonclick()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2nV8Mr60ZZMY"
      },
      "source": [
        "# 9번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3AqhZj1FZbk7"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "t.width(5)\n",
        "\n",
        "t.up()\n",
        "t.goto(-150, 0)\n",
        "t.down()\n",
        "t.color(\"blue\")\n",
        "t.circle(90)\n",
        "t.up()\n",
        "t.goto(0, 0)\n",
        "t.down()\n",
        "t.color(\"black\")\n",
        "t.circle(90)\n",
        "t.up()\n",
        "t.goto(-80, -100)\n",
        "t.down()\n",
        "t.color(\"yellow\")\n",
        "t.circle(90)\n",
        "t.up()\n",
        "t.goto(80, -100)\n",
        "t.down()\n",
        "t.color(\"green\")\n",
        "t.circle(90)\n",
        "t.up()\n",
        "t.goto(150, 0)\n",
        "t.down()\n",
        "t.color(\"red\")\n",
        "t.circle(90)\n",
        "t._screen.exitonclick()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J2d1NS6KWThL"
      },
      "source": [
        "\n",
        "\n",
        "# 도전문제\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "JhzPiZe126Hn"
      },
      "source": [
        "# 1번\n",
        "```\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yyrQ3MSj2Tax",
        "outputId": "fe2c7877-5004-455b-e85d-840b6f9ec45b"
      },
      "source": [
        "print(\"안녕하세요?\")\n",
        "print(\"programming에 입문하신 것을 축하드립니다.\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "안녕하세요?\n",
            "programming에 입문하신 것을 축하드립니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "43UBGW2u2_1f"
      },
      "source": [
        "# 2번\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IQDwu-Ar2uDZ",
        "outputId": "b8d91964-562d-45e8-d109-f414d76242b7"
      },
      "source": [
        "print(3.141592*10.0*10.0)\n",
        "print((1/100)*1234)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "314.1592\n",
            "12.34\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8xOYCwK_3Nhe"
      },
      "source": [
        "# 3-1번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bpUDMIWo3M58"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "\n",
        "t.forward(100)\n",
        "t.left(120)\n",
        "t.forward(100)\n",
        "t.left(120)\n",
        "t.forward(100)\n",
        "t.left(120)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LMORfQY03tbn"
      },
      "source": [
        "# 3-2번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XrU4iLlv33G6"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "\n",
        "t.forward(100)\n",
        "t.left(90)\n",
        "t.forward(100)\n",
        "t.left(90)\n",
        "t.forward(100)\n",
        "t.left(90)\n",
        "t.forward(100)\n",
        "t.left(90)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uLmBWK5U3vJ7"
      },
      "source": [
        "# 4번"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tT3sSHgc4JLJ"
      },
      "source": [
        "import turtle\n",
        "t = turtle.Turtle()\n",
        "t.shape(\"turtle\")\n",
        "\n",
        "t.forward(100)\n",
        "t.left(60)\n",
        "t.forward(100)\n",
        "t.left(60)\n",
        "t.forward(100)\n",
        "t.left(60)\n",
        "t.forward(100)\n",
        "t.left(60)\n",
        "t.forward(100)\n",
        "t.left(60)\n",
        "t.forward(100)\n",
        "t.left(60)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
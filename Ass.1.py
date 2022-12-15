{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0759f3b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter any 3 numbers\n",
      "4\n",
      "5\n",
      "6\n",
      "The average of the 3 numbers is 5.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Please enter any 3 numbers\")\n",
    "a=int(input())\n",
    "b=int(input())\n",
    "c=int(input())\n",
    "d=(a+b+c)/3\n",
    "print(\"The average of the 3 numbers is \"+str(d))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7dd0fc89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your gross salary\n",
      "60000\n",
      "Enter the number of dependents\n",
      "3\n",
      "Your taxable income is 41000\n",
      "Your tax is 20500.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter your gross salary\")\n",
    "a=int(input())\n",
    "print(\"Enter the number of dependents\")\n",
    "b=int(input())\n",
    "c=a-10000-(b*3000)\n",
    "print(\"Your taxable income is \"+str(c))\n",
    "print(\"Your tax is \"+str(c*0.5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2e94a946",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of seconds\n",
      "500\n",
      "Seconds = 8 minutes and 20 seconds\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter the number of seconds\")\n",
    "a=int(input())\n",
    "b=a//60\n",
    "c=a%60\n",
    "print(\"Seconds = \"+str(b)+\" minutes and \"+str(c)+\" seconds\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "62de497b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The sum is 75.0\n"
     ]
    }
   ],
   "source": [
    "a = str('25')\n",
    "b = int(25)\n",
    "c = float(25.0)\n",
    "d = float(a)+float(b)+float(c)\n",
    "print(\"The sum is \" +str(d))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a3bada1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sin of angle 0.0\n",
      "cosine of angle 1.0\n",
      "sin of angle 0.2588\n",
      "cosine of angle 0.9659\n",
      "sin of angle 0.5\n",
      "cosine of angle 0.866\n",
      "sin of angle 0.7071\n",
      "cosine of angle 0.7071\n",
      "sin of angle 0.866\n",
      "cosine of angle 0.5\n",
      "sin of angle 0.9659\n",
      "cosine of angle 0.2588\n",
      "sin of angle 1.0\n",
      "cosine of angle 0.0\n",
      "sin of angle 0.9659\n",
      "cosine of angle -0.2588\n",
      "sin of angle 0.866\n",
      "cosine of angle -0.5\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "a=0\n",
    "while a<=120:\n",
    "    b=a*(math.pi/180)\n",
    "    c=(math.sin(b))\n",
    "    d=(math.cos(b))\n",
    "    print(\"sin of angle\", (round(c,4)))\n",
    "    print(\"cosine of angle\", (round(d,4)))\n",
    "    a=a+15    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4aace850",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fec4fb64",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

U
    �4_h  �                   @   s@  d dl mZ d dlZd dlZd dlZd dlZd dlZd dlZdZe�	e� e�
d� e�
d� dZeed� zedd	�Ze�� Zej W n>   edd
�Ze�e� ej edd	�Ze�� Zej Y nX zedd	�Ze�� Zej W n>   edd
�Ze�e� ej edd	�Ze�� Zej Y nX z&edd	�Zedd	�Ze�� Zej W n>   edd
�Ze�e� ej edd	�Ze�� Zej Y nX zd dlZW nt ek
�r
   ed� e�
d� e�
d� e�
d� e�
d� e�
d� e�
d� ed� e�
d� d dlZY nX dd� Zed�Zed�Zdd� Zedk�r<e�  dS )�    )�ClientN�   �clearzgit pulluC  [1;32;40m
	 /$$$$$$$                  /$$ /$$   /$$             /$$
	| $$__  $$                | $$| $$$ | $$            | $$ 
	| $$  \ $$  /$$$$$$   /$$$$$$$| $$$$| $$  /$$$$$$  /$$$$$$ 
	| $$$$$$$/ /$$__  $$ /$$__  $$| $$ $$ $$ /$$__  $$|_  $$_/
	| $$__  $$| $$$$$$$$| $$  | $$| $$  $$$$| $$$$$$$$  | $$ 
	| $$  \ $$| $$_____/| $$  | $$| $$\  $$$| $$_____/  | $$ /$$ 
	| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$  |  $$$$/ 
	|__/  |__/ \_______/ \_______/|__/  \__/ \_______/   \___/

	 [¤] Termux Whatsapp Spam
	 [¤] Versions : 2.3.0
	 [¤] Coded By Shehan Lahiru
  � zspam.js�r�wzsid.jsztoken.jsz,%s Requests isn't installed, installing now.zpip3 install requestszpip3 install twiliozpip3 install matplotlibz%s Requests has been installed.c                   C   s2   t d� t d� t d� t d� t d� t�  d S )Nu(   [0;36m  ░P░A░N░D░O░R░A░z	[0;36m  u    [0;36m  ωнαтsαρρ sραмr   )�print�setup� r
   r
   �whatsapp.py�mainS   s    r   zEnter send message: zEnter a number: c            
      C   s�   t �d� ttd� t} t}d}d}t||�}|jjdt	t
d�}d}d|kr�t �d� tt� d}|d7 }td	�D ]@}|d	 d
 }	tdtt|	��d dd� t�d� tj�d� qrqDt �d� t�  d S )Nr   �
Z"ACccc5b0a8ad0202a78012e010bb926907Z 1feaef63b07744bbf6715ee212beb335zwhatsapp:+14155238886)Zfrom_Zbody�tor   r   �   �e   u   [1;36;40m
>>> [¤]z% r   )�endg�~j�t�x?z[F)�os�systemr   �name�sid�tokenr   ZmessagesZcreate�t�sr�range�str�int�time�sleep�sys�stdout�writer	   )
Z	irc_inputZ
irc_joinigZprint_inputZprint_outputZclient�messageZss�size�iZprr
   r
   r   r	   ]   s2    


�


r	   �__main__)Ztwilio.restr   r   r   r   ZurllibZpipZsocketZtimeoutZsetdefaulttimeoutr   r   r   �open�f�readZspam�closer    �wrr   r   �ImportErrorr   �inputr   r   r	   �__name__r
   r
   r
   r   �<module>   s�   


























!

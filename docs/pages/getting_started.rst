Getting Started
=======================
This page shows how to quickly get started with **cloudcord**.

Installing
-----------
Python 3.9 or higher is required.
::

    pip install cloudcord

You can also install the latest version from GitHub. Note that this version may be unstable.
::

    pip install git+https://github.com/littxle/cloudcord


First Steps
--------------
You should already have a basic understanding of **Discord.py** or **Pycord**.

1. Create a new bot in the `Discord Developer Portal <https://discord.com/developers/applications/>`_
2. Create a bot object using :doc:`cloudcord.Bot </cloudcord/bot>`

.. hint::
    If you are using Pycord with Prefix commands, use ``cloudcord.PrefixBot`` instead.


Example
--------------
A quick example of how cloudcord works. You can find more examples :doc:`here </examples/examples>`.

.. literalinclude:: ../../examples/pycord.py
   :language: python
   :caption: Pycord

.. literalinclude:: ../../examples/dpy.py
   :language: python
   :caption: Discord.py

Language
=======================
You can modify the default language files and even create your own language files.

.. note::

   The following languages are available by default:

   - English (``en``)
   - German (``de``)


Modify language files
---------------------

1. Create a JSON file with the prefix ``cl_`` somewhere in your project.

   - If you want to modify the English language file: ``cl_en.json``.
   - If you want to create a new language file: ``cl_[language].json``.

   For example, if you want to create a French language file, the file name could be ``cl_fr.json``.

2. Search the :ref:`language files <language>` and find keys you want to override.

   - Include any keys that you want to override in your JSON file.

3. Pass the language string into :meth:`~cloudcord.bot.Bot` to set your language.

.. code-block:: python

   bot = clcord.Bot(language="fr")  # French (loaded from cl_fr.json)


.. _language:

Language files
--------------

.. literalinclude:: ../../cloudcord/internal/language/en.json
   :language: python
   :caption: The default language file for English.

.. literalinclude:: ../../cloudcord/internal/language/de.json
   :language: python
   :caption: The default language file for German.

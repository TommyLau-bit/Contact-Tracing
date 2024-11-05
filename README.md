Project Description

This Python application analyzes contact tracing data to track virus spread within a dataset. It’s designed to identify infected individuals, potential “patient zero(s),” and others at risk. Each function tackles a different aspect of the tracing analysis, with a detailed breakdown for incremental completion.

Key Features

	1.	File Verification: Checks if the data file exists before running.
	2.	Data Parsing: Reads contact tracing data and organizes it into a dictionary with infected individuals as keys and their contacts as values.
	3.	Output Formatting: Uses a pretty_print_section_X() function for formatted console output.
	4.	Analysis Modules:
      	•	Identifies potential patient zero(s) (those not in anyone else’s contact list).
      	•	Lists “potential zombies” (contacts of infected individuals who haven’t shown symptoms).
      	•	Highlights individuals who aren’t “zombies” or “patients zero.”
      	•	Recognizes “most viral people” based on the number of contacts and “most contacted” individuals.
	5.	Distance Calculation: Calculates the maximum distance from any potential zombie in the contact chain.

Additional Credit Challenges

	•	Zombie Classification: Detects spreader, regular, and predator zombies.
	•	Cycle Detection: Identifies cycles in data to prevent infinite loops during distance calculations.

Testing and Submission

	•	Deadline: March 27, 2023, at 16:00 (UK time).
	•	Submission: Only submit the .py file via Moodle.
	•	Testing: Use the UCL webform for testing. Ensure your code aligns exactly with expected outputs and follows the specified Python style guide.

Style Guidelines

	•	Adhere to Python conventions: snake_case for variables/functions, and appropriate variable naming.
	•	Use consistent indentation and avoid break or continue within loops.
	•	Each function should include docstrings for clarity on parameters and return values.

Important Notes on Plagiarism

	•	Cite any non-original code.
	•	Ensure individual work; sharing or copying code will lead to plagiarism detection.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_LENGTH 255

//Combine File1 and File2 into outputFile, one line at a time
void combineCsvs(char *inputFile1, char *inputFile2, char *outputFile, int index)
{

	FILE *filePointer1;
	FILE *filePointer2;
	FILE *filePointer3;

	//Open the input files for reading, and the output file for writing
	filePointer1 = fopen(inputFile1, "r");
	filePointer2 = fopen(inputFile2, "r");
	filePointer3 = fopen(outputFile, "a");

	if (filePointer1 == NULL || filePointer2 == NULL)
	{
		printf("Error reading from files!\n");
		return;
	}

	//These keep track of whether we've reached the end of the file
	void* endOfFile1 = 0;
	void* endOfFile2 = 0;


	char currLine[LINE_LENGTH];

	char indexAsString[LINE_LENGTH];
	sprintf(indexAsString, "%d", index);
	strcat(indexAsString, ",");

	//Read and write to files, while the input files still have lines left
	do
	{
		//Read a line from input file 1
		endOfFile1 = fgets(currLine, LINE_LENGTH, filePointer1);
		if (endOfFile1 != NULL){
			//printf("Curr line from file 1: %s \n", currLine);
			strcat(indexAsString, currLine);
			fprintf(filePointer3, indexAsString);
			sprintf(indexAsString, "%d", index);
			strcat(indexAsString, ",");
		}

		//Read a line from input file 2
		endOfFile2 = fgets(currLine, LINE_LENGTH, filePointer2);
		if (endOfFile2 != NULL){
			//printf("Curr line from file 2: %s \n", currLine);
			strcat(indexAsString, currLine);
			fprintf(filePointer3, indexAsString);
			sprintf(indexAsString, "%d", index);
			strcat(indexAsString, ",");
		}

    } while(endOfFile1 != NULL || endOfFile2 != NULL);

	//Close the files
    fclose(filePointer1);
	fclose(filePointer2);
	fclose(filePointer3);
}

//Command line arguments should be of form
//argv[1] = pathToInputFile1
//argv[2] = pathToInputFile2
//argv[3] = pathToInputFile3
int main(int argc, char **argv)
{
	/*
	int b = 0;
	int c = 0;
	int loops = 99999;
	for(int i = 0; i < loops; i++)
	{
		for(int j = 0; j < loops; j++)
		{
			b = 1-b;
		}

		c++;
		if(c == 1000)
		{
			printf("C incremented");
			c = 0;
		}
	}*/


	if (argc != 4)
	{
		printf("You must provide three file paths to perform csv combination! (file1, file2, and destination)\n");
		return 0;
	}

	for(int i = 0; i < 25000; i++)
	{

		combineCsvs(argv[1], argv[2], argv[3], i);
	}

	return 0;
}


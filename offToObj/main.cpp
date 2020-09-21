#include <iostream> //���û��pcl���������Ϊ����cout��ͷ�ļ�
#include <fstream>

using namespace std;
float vertex[300000][3];
int surface[300000][3];

void read_off_file(string input)
{
	//��������˵������ȡoff�ļ�  �ļ�����Ҫͬʱ����off��obj�ļ� ����д��obj
	char k;
	int vertex_num;
	int surface_num;
	int other_num;
	int i, j;
	int s;
	ifstream fin;
	ofstream fout;
	fin.open(input + ".off");
	while (fin.fail())
	{
		cout << "Fail to open the off file!" << endl;
		exit(1);
	}
	fout.open(input + ".obj");//����ļ�
	while (fout.fail())
	{
		cout << "Fail to open the obj file!" << endl;
		exit(1);
	}
	do
	{
		cout << fin.get();
	} while (fin.get() != '\n');
	fin >> vertex_num >> surface_num >> other_num;
	cout << vertex_num;
	for (i = 0; i < vertex_num; i++)
	{
		for (j = 0; j < 3; j++)
		{
			fin >> vertex[i][j];
		}
	}
	for (i = 0; i < surface_num; i++)
	{
		fin >> s;
		cout << s << endl;
		for (j = 0; j < 3; j++)
		{
			fin >> surface[i][j];
		}
	}

	for (i = 0; i < vertex_num; i++)
	{
		fout.put('v');
		fout.put(' ');
		for (j = 0; j < 3; j++)
		{
			fout << vertex[i][j];
			fout.put(' ');
		}
		fout.put('\n');

	}
	fout.put('\n'); //ע����ƻ���

	for (i = 0; i < surface_num; i++)
	{
		fout.put('f');
		fout.put(' ');
		for (j = 0; j < 3; j++)
		{
			fout << (surface[i][j] + 1);
			fout.put(' ');
		}
		fout.put('\n');
	}
	fin.close();
	fout.close();
	cout << "end" << endl;
}

int main(int argc, char **argv)
{
	//��������
	read_off_file("LSCM_bunny_result"); //������Ҫ���ļ���������׺
	return 0;
}

#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_3_4_8_86_32_10_4(Basic_Sfuncs* bs) {
  return new VP2_3_4_8_86_32_10_4(bs);
}

VP2_3_4_8_86_32_10_4::VP2_3_4_8_86_32_10_4(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[3];
  c = new Complex[8];
  Z = new Complex[86];
  M = new Complex*[32];
  for(int i=0;i<32;i++) M[i] = new Complex[2];
  cl = new int[32];
}

VP2_3_4_8_86_32_10_4::~VP2_3_4_8_86_32_10_4()
{
  if (Z)  delete[] Z;
  if (f)  delete[] f;
  if (c)  delete[] c;
  if (cl) delete[] cl;
  if (M) {
    for(int i=0;i<32;i++) delete[] M[i];
    delete[] M;
  }
}

Complex VP2_3_4_8_86_32_10_4::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 2: Calculate_M2(); break;
    case 3: Calculate_M3(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
    case 14: Calculate_M14(); break;
    case 15: Calculate_M15(); break;
    case 16: Calculate_M16(); break;
    case 17: Calculate_M17(); break;
    case 18: Calculate_M18(); break;
    case 19: Calculate_M19(); break;
    case 28: Calculate_M28(); break;
    case 29: Calculate_M29(); break;
    case 30: Calculate_M30(); break;
    case 31: Calculate_M31(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void VP2_3_4_8_86_32_10_4::Calculate_M0()
{
  M[0][0] = Z[21]*Z[16]*Z[15];
  M[0][1] = (Z[31]*Z[30]-Z[22]*Z[15])*Z[32];
}

void VP2_3_4_8_86_32_10_4::Calculate_M1()
{
  M[1][0] = Z[21]*Z[16]*Z[26];
  M[1][1] = (Z[45]*Z[30]-Z[22]*Z[26])*Z[32];
}

void VP2_3_4_8_86_32_10_4::Calculate_M2()
{
  M[2][0] = -(Z[46]*Z[11]-Z[16]*Z[20])*Z[21];
  M[2][1] = -Z[32]*Z[22]*Z[20];
}

void VP2_3_4_8_86_32_10_4::Calculate_M3()
{
  M[3][0] = -(Z[46]*Z[40]-Z[16]*Z[44])*Z[21];
  M[3][1] = -Z[32]*Z[22]*Z[44];
}

void VP2_3_4_8_86_32_10_4::Calculate_M12()
{
  M[12][0] = Z[21]*Z[16]*Z[59];
  M[12][1] = (Z[31]*Z[68]-Z[22]*Z[59])*Z[32];
}

void VP2_3_4_8_86_32_10_4::Calculate_M13()
{
  M[13][0] = Z[21]*Z[16]*Z[65];
  M[13][1] = (Z[45]*Z[68]-Z[22]*Z[65])*Z[32];
}

void VP2_3_4_8_86_32_10_4::Calculate_M14()
{
  M[14][0] = -(Z[46]*Z[56]-Z[16]*Z[62])*Z[21];
  M[14][1] = -Z[32]*Z[22]*Z[62];
}

void VP2_3_4_8_86_32_10_4::Calculate_M15()
{
  M[15][0] = -(Z[46]*Z[74]-Z[16]*Z[77])*Z[21];
  M[15][1] = -Z[32]*Z[22]*Z[77];
}

void VP2_3_4_8_86_32_10_4::Calculate_M16()
{
  M[16][0] = -(Z[81]*Z[7]-Z[82]*Z[15])*Z[21];
  M[16][1] = -Z[32]*Z[83]*Z[15];
}

void VP2_3_4_8_86_32_10_4::Calculate_M17()
{
  M[17][0] = -(Z[81]*Z[36]-Z[82]*Z[26])*Z[21];
  M[17][1] = -Z[32]*Z[83]*Z[26];
}

void VP2_3_4_8_86_32_10_4::Calculate_M18()
{
  M[18][0] = Z[21]*Z[82]*Z[20];
  M[18][1] = (Z[84]*Z[50]-Z[83]*Z[20])*Z[32];
}

void VP2_3_4_8_86_32_10_4::Calculate_M19()
{
  M[19][0] = Z[21]*Z[82]*Z[44];
  M[19][1] = (Z[85]*Z[50]-Z[83]*Z[44])*Z[32];
}

void VP2_3_4_8_86_32_10_4::Calculate_M28()
{
  M[28][0] = -(Z[81]*Z[53]-Z[82]*Z[59])*Z[21];
  M[28][1] = -Z[32]*Z[83]*Z[59];
}

void VP2_3_4_8_86_32_10_4::Calculate_M29()
{
  M[29][0] = -(Z[81]*Z[71]-Z[82]*Z[65])*Z[21];
  M[29][1] = -Z[32]*Z[83]*Z[65];
}

void VP2_3_4_8_86_32_10_4::Calculate_M30()
{
  M[30][0] = Z[21]*Z[82]*Z[62];
  M[30][1] = (Z[84]*Z[80]-Z[83]*Z[62])*Z[32];
}

void VP2_3_4_8_86_32_10_4::Calculate_M31()
{
  M[31][0] = Z[21]*Z[82]*Z[77];
  M[31][1] = (Z[85]*Z[80]-Z[83]*Z[77])*Z[32];
}


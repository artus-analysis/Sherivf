#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_3_4_8_60_32_10_0(Basic_Sfuncs* bs) {
  return new VP2_3_4_8_60_32_10_0(bs);
}

VP2_3_4_8_60_32_10_0::VP2_3_4_8_60_32_10_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[3];
  c = new Complex[8];
  Z = new Complex[60];
  M = new Complex*[32];
  for(int i=0;i<32;i++) M[i] = new Complex[2];
  cl = new int[32];
}

VP2_3_4_8_60_32_10_0::~VP2_3_4_8_60_32_10_0()
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

Complex VP2_3_4_8_60_32_10_0::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 2: Calculate_M2(); break;
    case 12: Calculate_M12(); break;
    case 14: Calculate_M14(); break;
    case 17: Calculate_M17(); break;
    case 19: Calculate_M19(); break;
    case 29: Calculate_M29(); break;
    case 31: Calculate_M31(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void VP2_3_4_8_60_32_10_0::Calculate_M0()
{
  M[0][0] = -Z[14]*Z[13]*Z[12];
  M[0][1] = -(Z[20]*Z[7]-Z[19]*Z[18])*Z[21];
}

void VP2_3_4_8_60_32_10_0::Calculate_M2()
{
  M[2][0] = -Z[14]*Z[32]*Z[12];
  M[2][1] = -(Z[34]*Z[7]-Z[33]*Z[18])*Z[21];
}

void VP2_3_4_8_60_32_10_0::Calculate_M12()
{
  M[12][0] = -Z[14]*Z[13]*Z[41];
  M[12][1] = -(Z[20]*Z[38]-Z[19]*Z[44])*Z[21];
}

void VP2_3_4_8_60_32_10_0::Calculate_M14()
{
  M[14][0] = -Z[14]*Z[32]*Z[41];
  M[14][1] = -(Z[34]*Z[38]-Z[33]*Z[44])*Z[21];
}

void VP2_3_4_8_60_32_10_0::Calculate_M17()
{
  M[17][0] = -Z[14]*Z[22]*Z[54];
  M[17][1] = -(Z[20]*Z[30]-Z[55]*Z[26])*Z[21];
}

void VP2_3_4_8_60_32_10_0::Calculate_M19()
{
  M[19][0] = -Z[14]*Z[35]*Z[54];
  M[19][1] = -(Z[34]*Z[30]-Z[56]*Z[26])*Z[21];
}

void VP2_3_4_8_60_32_10_0::Calculate_M29()
{
  M[29][0] = -Z[14]*Z[22]*Z[59];
  M[29][1] = -(Z[20]*Z[50]-Z[55]*Z[47])*Z[21];
}

void VP2_3_4_8_60_32_10_0::Calculate_M31()
{
  M[31][0] = -Z[14]*Z[35]*Z[59];
  M[31][1] = -(Z[34]*Z[50]-Z[56]*Z[47])*Z[21];
}


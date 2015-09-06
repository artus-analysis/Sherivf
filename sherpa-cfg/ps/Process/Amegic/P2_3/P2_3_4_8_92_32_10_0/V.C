#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_VP2_3_4_8_92_32_10_0(Basic_Sfuncs* bs) {
  return new VP2_3_4_8_92_32_10_0(bs);
}

VP2_3_4_8_92_32_10_0::VP2_3_4_8_92_32_10_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[3];
  c = new Complex[8];
  Z = new Complex[92];
  M = new Complex*[32];
  for(int i=0;i<32;i++) M[i] = new Complex[2];
  cl = new int[32];
}

VP2_3_4_8_92_32_10_0::~VP2_3_4_8_92_32_10_0()
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

Complex VP2_3_4_8_92_32_10_0::Evaluate(int m,int n)
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

void VP2_3_4_8_92_32_10_0::Calculate_M0()
{
  M[0][0] = -Z[19]*Z[17]*Z[16];
  M[0][1] = -(Z[29]*Z[7]-Z[24]*Z[23])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M1()
{
  M[1][0] = -Z[19]*Z[35]*Z[16];
  M[1][1] = -(Z[29]*Z[12]-Z[24]*Z[40])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M2()
{
  M[2][0] = -Z[19]*Z[50]*Z[16];
  M[2][1] = -(Z[53]*Z[7]-Z[52]*Z[23])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M3()
{
  M[3][0] = -Z[19]*Z[54]*Z[16];
  M[3][1] = -(Z[53]*Z[12]-Z[52]*Z[40])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M12()
{
  M[12][0] = -Z[19]*Z[17]*Z[64];
  M[12][1] = -(Z[29]*Z[58]-Z[24]*Z[67])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M13()
{
  M[13][0] = -Z[19]*Z[35]*Z[64];
  M[13][1] = -(Z[29]*Z[61]-Z[24]*Z[76])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M14()
{
  M[14][0] = -Z[19]*Z[50]*Z[64];
  M[14][1] = -(Z[53]*Z[58]-Z[52]*Z[67])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M15()
{
  M[15][0] = -Z[19]*Z[54]*Z[64];
  M[15][1] = -(Z[53]*Z[61]-Z[52]*Z[76])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M16()
{
  M[16][0] = -Z[19]*Z[18]*Z[86];
  M[16][1] = -(Z[29]*Z[33]-Z[87]*Z[28])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M17()
{
  M[17][0] = -Z[19]*Z[36]*Z[86];
  M[17][1] = -(Z[29]*Z[48]-Z[87]*Z[44])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M18()
{
  M[18][0] = -Z[19]*Z[51]*Z[86];
  M[18][1] = -(Z[53]*Z[33]-Z[88]*Z[28])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M19()
{
  M[19][0] = -Z[19]*Z[55]*Z[86];
  M[19][1] = -(Z[53]*Z[48]-Z[88]*Z[44])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M28()
{
  M[28][0] = -Z[19]*Z[18]*Z[91];
  M[28][1] = -(Z[29]*Z[73]-Z[87]*Z[70])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M29()
{
  M[29][0] = -Z[19]*Z[36]*Z[91];
  M[29][1] = -(Z[29]*Z[82]-Z[87]*Z[79])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M30()
{
  M[30][0] = -Z[19]*Z[51]*Z[91];
  M[30][1] = -(Z[53]*Z[73]-Z[88]*Z[70])*Z[34];
}

void VP2_3_4_8_92_32_10_0::Calculate_M31()
{
  M[31][0] = -Z[19]*Z[55]*Z[91];
  M[31][1] = -(Z[53]*Z[82]-Z[88]*Z[79])*Z[34];
}


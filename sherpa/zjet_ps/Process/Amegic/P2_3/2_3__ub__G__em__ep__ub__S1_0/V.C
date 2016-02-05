#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_3__ub__G__em__ep__ub__S1_0(Basic_Sfuncs* bs) {
  return new V2_3__ub__G__em__ep__ub__S1_0(bs);
}

V2_3__ub__G__em__ep__ub__S1_0::V2_3__ub__G__em__ep__ub__S1_0(Basic_Sfuncs* _BS) :
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

V2_3__ub__G__em__ep__ub__S1_0::~V2_3__ub__G__em__ep__ub__S1_0()
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

Complex V2_3__ub__G__em__ep__ub__S1_0::Evaluate(int m,int n)
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

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M0()
{
  M[0][0] = -(Z[8]*Z[7]-Z[17]*Z[16])*Z[22];
  M[0][1] = -Z[34]*Z[32]*Z[31];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M1()
{
  M[1][0] = -(Z[8]*Z[27]-Z[17]*Z[42])*Z[22];
  M[1][1] = -Z[34]*Z[47]*Z[31];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M2()
{
  M[2][0] = -(Z[49]*Z[7]-Z[50]*Z[16])*Z[22];
  M[2][1] = -Z[34]*Z[52]*Z[31];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M3()
{
  M[3][0] = -(Z[49]*Z[27]-Z[50]*Z[42])*Z[22];
  M[3][1] = -Z[34]*Z[54]*Z[31];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M12()
{
  M[12][0] = -(Z[8]*Z[58]-Z[17]*Z[64])*Z[22];
  M[12][1] = -Z[34]*Z[32]*Z[73];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M13()
{
  M[13][0] = -(Z[8]*Z[70]-Z[17]*Z[79])*Z[22];
  M[13][1] = -Z[34]*Z[47]*Z[73];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M14()
{
  M[14][0] = -(Z[49]*Z[58]-Z[50]*Z[64])*Z[22];
  M[14][1] = -Z[34]*Z[52]*Z[73];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M15()
{
  M[15][0] = -(Z[49]*Z[70]-Z[50]*Z[79])*Z[22];
  M[15][1] = -Z[34]*Z[54]*Z[73];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M16()
{
  M[16][0] = -(Z[8]*Z[12]-Z[83]*Z[21])*Z[22];
  M[16][1] = -Z[34]*Z[33]*Z[87];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M17()
{
  M[17][0] = -(Z[8]*Z[38]-Z[83]*Z[46])*Z[22];
  M[17][1] = -Z[34]*Z[48]*Z[87];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M18()
{
  M[18][0] = -(Z[49]*Z[12]-Z[88]*Z[21])*Z[22];
  M[18][1] = -Z[34]*Z[53]*Z[87];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M19()
{
  M[19][0] = -(Z[49]*Z[38]-Z[88]*Z[46])*Z[22];
  M[19][1] = -Z[34]*Z[55]*Z[87];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M28()
{
  M[28][0] = -(Z[8]*Z[61]-Z[83]*Z[67])*Z[22];
  M[28][1] = -Z[34]*Z[33]*Z[91];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M29()
{
  M[29][0] = -(Z[8]*Z[76]-Z[83]*Z[82])*Z[22];
  M[29][1] = -Z[34]*Z[48]*Z[91];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M30()
{
  M[30][0] = -(Z[49]*Z[61]-Z[88]*Z[67])*Z[22];
  M[30][1] = -Z[34]*Z[53]*Z[91];
}

void V2_3__ub__G__em__ep__ub__S1_0::Calculate_M31()
{
  M[31][0] = -(Z[49]*Z[76]-Z[88]*Z[82])*Z[22];
  M[31][1] = -Z[34]*Z[55]*Z[91];
}


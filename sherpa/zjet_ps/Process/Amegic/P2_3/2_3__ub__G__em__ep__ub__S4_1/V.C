#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_3__ub__G__em__ep__ub__S4_1(Basic_Sfuncs* bs) {
  return new V2_3__ub__G__em__ep__ub__S4_1(bs);
}

V2_3__ub__G__em__ep__ub__S4_1::V2_3__ub__G__em__ep__ub__S4_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[3];
  c = new Complex[8];
  Z = new Complex[54];
  M = new Complex*[32];
  for(int i=0;i<32;i++) M[i] = new Complex[2];
  cl = new int[32];
}

V2_3__ub__G__em__ep__ub__S4_1::~V2_3__ub__G__em__ep__ub__S4_1()
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

Complex V2_3__ub__G__em__ep__ub__S4_1::Evaluate(int m,int n)
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

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M0()
{
  M[0][0] = -(Z[8]*Z[7]-Z[13]*Z[12])*Z[14];
}

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M2()
{
  M[2][0] = -Z[14]*Z[29]*Z[7];
  M[2][1] = -Z[19]*Z[30]*Z[18];
}

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M12()
{
  M[12][0] = -(Z[8]*Z[33]-Z[13]*Z[36])*Z[14];
}

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M14()
{
  M[14][0] = -Z[14]*Z[29]*Z[33];
  M[14][1] = -Z[19]*Z[30]*Z[39];
}

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M17()
{
  M[17][0] = -Z[14]*Z[8]*Z[23];
  M[17][1] = -Z[19]*Z[28]*Z[49];
}

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M19()
{
  M[19][0] = -(Z[29]*Z[23]-Z[50]*Z[27])*Z[14];
}

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M29()
{
  M[29][0] = -Z[14]*Z[8]*Z[42];
  M[29][1] = -Z[19]*Z[28]*Z[53];
}

void V2_3__ub__G__em__ep__ub__S4_1::Calculate_M31()
{
  M[31][0] = -(Z[29]*Z[42]-Z[50]*Z[45])*Z[14];
}


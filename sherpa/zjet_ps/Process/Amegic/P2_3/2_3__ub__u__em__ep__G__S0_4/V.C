#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_3__ub__u__em__ep__G__S0_4(Basic_Sfuncs* bs) {
  return new V2_3__ub__u__em__ep__G__S0_4(bs);
}

V2_3__ub__u__em__ep__G__S0_4::V2_3__ub__u__em__ep__G__S0_4(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[3];
  c = new Complex[8];
  Z = new Complex[56];
  M = new Complex*[32];
  for(int i=0;i<32;i++) M[i] = new Complex[2];
  cl = new int[32];
}

V2_3__ub__u__em__ep__G__S0_4::~V2_3__ub__u__em__ep__G__S0_4()
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

Complex V2_3__ub__u__em__ep__G__S0_4::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 3: Calculate_M3(); break;
    case 12: Calculate_M12(); break;
    case 15: Calculate_M15(); break;
    case 16: Calculate_M16(); break;
    case 19: Calculate_M19(); break;
    case 28: Calculate_M28(); break;
    case 31: Calculate_M31(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M0()
{
  M[0][0] = -Z[13]*Z[8]*Z[7];
  M[0][1] = -(Z[19]*Z[18]-Z[14]*Z[7])*Z[20];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M3()
{
  M[3][0] = (Z[21]*Z[33]-Z[8]*Z[25])*Z[13];
  M[3][1] = Z[20]*Z[14]*Z[25];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M12()
{
  M[12][0] = -Z[13]*Z[8]*Z[36];
  M[12][1] = -(Z[19]*Z[42]-Z[14]*Z[36])*Z[20];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M15()
{
  M[15][0] = (Z[21]*Z[51]-Z[8]*Z[45])*Z[13];
  M[15][1] = Z[20]*Z[14]*Z[45];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M16()
{
  M[16][0] = (Z[53]*Z[12]-Z[52]*Z[7])*Z[13];
  M[16][1] = Z[20]*Z[54]*Z[7];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M19()
{
  M[19][0] = -Z[13]*Z[52]*Z[25];
  M[19][1] = -(Z[55]*Z[29]-Z[54]*Z[25])*Z[20];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M28()
{
  M[28][0] = (Z[53]*Z[39]-Z[52]*Z[36])*Z[13];
  M[28][1] = Z[20]*Z[54]*Z[36];
}

void V2_3__ub__u__em__ep__G__S0_4::Calculate_M31()
{
  M[31][0] = -Z[13]*Z[52]*Z[45];
  M[31][1] = -(Z[55]*Z[48]-Z[54]*Z[45])*Z[20];
}


#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_3__G__u__em__ep__u__S0_1(Basic_Sfuncs* bs) {
  return new V2_3__G__u__em__ep__u__S0_1(bs);
}

V2_3__G__u__em__ep__u__S0_1::V2_3__G__u__em__ep__u__S0_1(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Xfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[3];
  c = new Complex[8];
  Z = new Complex[95];
  M = new Complex*[32];
  for(int i=0;i<32;i++) M[i] = new Complex[2];
  cl = new int[32];
}

V2_3__G__u__em__ep__u__S0_1::~V2_3__G__u__em__ep__u__S0_1()
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

Complex V2_3__G__u__em__ep__u__S0_1::Evaluate(int m,int n)
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

void V2_3__G__u__em__ep__u__S0_1::Calculate_M0()
{
  M[0][0] = -Z[18]*Z[8]*Z[7];
  M[0][1] = -(Z[29]*Z[17]-Z[23]*Z[22])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M1()
{
  M[1][0] = -Z[18]*Z[31]*Z[7];
  M[1][1] = -(Z[36]*Z[17]-Z[34]*Z[22])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M2()
{
  M[2][0] = -(Z[38]*Z[12]+Z[37]*Z[7])*Z[18];
  M[2][1] = (Z[28]*Z[46]+Z[23]*Z[42])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M3()
{
  M[3][0] = -(Z[52]*Z[12]+Z[51]*Z[7])*Z[18];
  M[3][1] = (Z[35]*Z[46]+Z[34]*Z[42])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M12()
{
  M[12][0] = -Z[18]*Z[8]*Z[55];
  M[12][1] = -(Z[29]*Z[61]-Z[23]*Z[64])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M13()
{
  M[13][0] = -Z[18]*Z[31]*Z[55];
  M[13][1] = -(Z[36]*Z[61]-Z[34]*Z[64])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M14()
{
  M[14][0] = -(Z[38]*Z[58]+Z[37]*Z[55])*Z[18];
  M[14][1] = (Z[28]*Z[73]+Z[23]*Z[70])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M15()
{
  M[15][0] = -(Z[52]*Z[58]+Z[51]*Z[55])*Z[18];
  M[15][1] = (Z[35]*Z[73]+Z[34]*Z[70])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M16()
{
  M[16][0] = -(Z[13]*Z[84]+Z[8]*Z[80])*Z[18];
  M[16][1] = (Z[86]*Z[27]+Z[85]*Z[22])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M17()
{
  M[17][0] = -(Z[32]*Z[84]+Z[31]*Z[80])*Z[18];
  M[17][1] = (Z[88]*Z[27]+Z[87]*Z[22])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M18()
{
  M[18][0] = -Z[18]*Z[38]*Z[84];
  M[18][1] = -(Z[29]*Z[50]-Z[86]*Z[46])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M19()
{
  M[19][0] = -Z[18]*Z[52]*Z[84];
  M[19][1] = -(Z[36]*Z[50]-Z[88]*Z[46])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M28()
{
  M[28][0] = -(Z[13]*Z[94]+Z[8]*Z[91])*Z[18];
  M[28][1] = (Z[86]*Z[67]+Z[85]*Z[64])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M29()
{
  M[29][0] = -(Z[32]*Z[94]+Z[31]*Z[91])*Z[18];
  M[29][1] = (Z[88]*Z[67]+Z[87]*Z[64])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M30()
{
  M[30][0] = -Z[18]*Z[38]*Z[94];
  M[30][1] = -(Z[29]*Z[76]-Z[86]*Z[73])*Z[30];
}

void V2_3__G__u__em__ep__u__S0_1::Calculate_M31()
{
  M[31][0] = -Z[18]*Z[52]*Z[94];
  M[31][1] = -(Z[36]*Z[76]-Z[88]*Z[73])*Z[30];
}


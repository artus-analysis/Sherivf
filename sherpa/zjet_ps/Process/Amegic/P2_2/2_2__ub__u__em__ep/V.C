#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_2__ub__u__em__ep(Basic_Sfuncs* bs) {
  return new V2_2__ub__u__em__ep(bs);
}

V2_2__ub__u__em__ep::V2_2__ub__u__em__ep(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[2];
  c = new Complex[6];
  Z = new Complex[22];
  M = new Complex*[16];
  for(int i=0;i<16;i++) M[i] = new Complex[2];
  cl = new int[16];
}

V2_2__ub__u__em__ep::~V2_2__ub__u__em__ep()
{
  if (Z)  delete[] Z;
  if (f)  delete[] f;
  if (c)  delete[] c;
  if (cl) delete[] cl;
  if (M) {
    for(int i=0;i<16;i++) delete[] M[i];
    delete[] M;
  }
}

Complex V2_2__ub__u__em__ep::Evaluate(int m,int n)
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
  }
  cl[n]=1;
  return M[n][m];
}

void V2_2__ub__u__em__ep::Calculate_M0()
{
  M[0][0] = Z[1]*Z[2];
  M[0][1] = Z[4]*Z[5];
}

void V2_2__ub__u__em__ep::Calculate_M1()
{
  M[1][0] = Z[6]*Z[2];
  M[1][1] = Z[8]*Z[5];
}

void V2_2__ub__u__em__ep::Calculate_M2()
{
  M[2][0] = Z[9]*Z[2];
  M[2][1] = Z[11]*Z[5];
}

void V2_2__ub__u__em__ep::Calculate_M3()
{
  M[3][0] = Z[12]*Z[2];
  M[3][1] = Z[13]*Z[5];
}

void V2_2__ub__u__em__ep::Calculate_M12()
{
  M[12][0] = Z[14]*Z[2];
  M[12][1] = Z[15]*Z[5];
}

void V2_2__ub__u__em__ep::Calculate_M13()
{
  M[13][0] = Z[16]*Z[2];
  M[13][1] = Z[17]*Z[5];
}

void V2_2__ub__u__em__ep::Calculate_M14()
{
  M[14][0] = Z[18]*Z[2];
  M[14][1] = Z[19]*Z[5];
}

void V2_2__ub__u__em__ep::Calculate_M15()
{
  M[15][0] = Z[20]*Z[2];
  M[15][1] = Z[21]*Z[5];
}


#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_3__G__u__em__ep__u__S4_0(Basic_Sfuncs* bs) {
  return new V2_3__G__u__em__ep__u__S4_0(bs);
}

V2_3__G__u__em__ep__u__S4_0::V2_3__G__u__em__ep__u__S4_0(Basic_Sfuncs* _BS) :
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

V2_3__G__u__em__ep__u__S4_0::~V2_3__G__u__em__ep__u__S4_0()
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

Complex V2_3__G__u__em__ep__u__S4_0::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 1: Calculate_M1(); break;
    case 12: Calculate_M12(); break;
    case 13: Calculate_M13(); break;
    case 18: Calculate_M18(); break;
    case 19: Calculate_M19(); break;
    case 30: Calculate_M30(); break;
    case 31: Calculate_M31(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M0()
{
  M[0][0] = -Z[13]*Z[8]*Z[7];
  M[0][1] = -Z[19]*Z[18]*Z[12];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M1()
{
  M[1][1] = -(Z[21]*Z[12]-Z[20]*Z[17])*Z[19];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M12()
{
  M[12][0] = -Z[13]*Z[8]*Z[33];
  M[12][1] = -Z[19]*Z[18]*Z[36];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M13()
{
  M[13][1] = -(Z[21]*Z[36]-Z[20]*Z[39])*Z[19];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M18()
{
  M[18][1] = -(Z[18]*Z[29]-Z[50]*Z[25])*Z[19];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M19()
{
  M[19][0] = -Z[13]*Z[30]*Z[49];
  M[19][1] = -Z[19]*Z[21]*Z[29];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M30()
{
  M[30][1] = -(Z[18]*Z[45]-Z[50]*Z[42])*Z[19];
}

void V2_3__G__u__em__ep__u__S4_0::Calculate_M31()
{
  M[31][0] = -Z[13]*Z[30]*Z[53];
  M[31][1] = -Z[19]*Z[21]*Z[45];
}


#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_3__G__db__em__ep__db__S4_1(Basic_Sfuncs* bs) {
  return new V2_3__G__db__em__ep__db__S4_1(bs);
}

V2_3__G__db__em__ep__db__S4_1::V2_3__G__db__em__ep__db__S4_1(Basic_Sfuncs* _BS) :
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

V2_3__G__db__em__ep__db__S4_1::~V2_3__G__db__em__ep__db__S4_1()
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

Complex V2_3__G__db__em__ep__db__S4_1::Evaluate(int m,int n)
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

void V2_3__G__db__em__ep__db__S4_1::Calculate_M0()
{
  M[0][0] = -(Z[13]*Z[12]-Z[8]*Z[7])*Z[14];
}

void V2_3__G__db__em__ep__db__S4_1::Calculate_M1()
{
  M[1][0] = -Z[14]*Z[20]*Z[12];
  M[1][1] = -Z[19]*Z[21]*Z[18];
}

void V2_3__G__db__em__ep__db__S4_1::Calculate_M12()
{
  M[12][0] = -(Z[13]*Z[36]-Z[8]*Z[33])*Z[14];
}

void V2_3__G__db__em__ep__db__S4_1::Calculate_M13()
{
  M[13][0] = -Z[14]*Z[20]*Z[36];
  M[13][1] = -Z[19]*Z[21]*Z[39];
}

void V2_3__G__db__em__ep__db__S4_1::Calculate_M18()
{
  M[18][0] = -Z[14]*Z[13]*Z[29];
  M[18][1] = -Z[19]*Z[30]*Z[49];
}

void V2_3__G__db__em__ep__db__S4_1::Calculate_M19()
{
  M[19][0] = -(Z[20]*Z[29]-Z[50]*Z[25])*Z[14];
}

void V2_3__G__db__em__ep__db__S4_1::Calculate_M30()
{
  M[30][0] = -Z[14]*Z[13]*Z[45];
  M[30][1] = -Z[19]*Z[30]*Z[53];
}

void V2_3__G__db__em__ep__db__S4_1::Calculate_M31()
{
  M[31][0] = -(Z[20]*Z[45]-Z[50]*Z[42])*Z[14];
}


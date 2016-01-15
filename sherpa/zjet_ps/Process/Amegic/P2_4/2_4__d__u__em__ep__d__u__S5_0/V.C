#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__d__u__em__ep__d__u__S5_0(Basic_Sfuncs* bs) {
  return new V2_4__d__u__em__ep__d__u__S5_0(bs);
}

V2_4__d__u__em__ep__d__u__S5_0::V2_4__d__u__em__ep__d__u__S5_0(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[5];
  c = new Complex[10];
  Z = new Complex[174];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[4];
  cl = new int[64];
}

V2_4__d__u__em__ep__d__u__S5_0::~V2_4__d__u__em__ep__d__u__S5_0()
{
  if (Z)  delete[] Z;
  if (f)  delete[] f;
  if (c)  delete[] c;
  if (cl) delete[] cl;
  if (M) {
    for(int i=0;i<64;i++) delete[] M[i];
    delete[] M;
  }
}

Complex V2_4__d__u__em__ep__d__u__S5_0::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 12: Calculate_M12(); break;
    case 17: Calculate_M17(); break;
    case 29: Calculate_M29(); break;
    case 34: Calculate_M34(); break;
    case 46: Calculate_M46(); break;
    case 51: Calculate_M51(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M0()
{
  M[0][0] = -(Z[10]*Z[9]+Z[15]*Z[14])*Z[18];
  M[0][1] = (Z[27]*Z[26]-Z[15]*Z[22])*Z[31];
  M[0][2] = -(Z[38]*Z[34]+Z[42]*Z[15])*Z[45];
  M[0][3] = -(Z[54]*Z[53]+Z[59]*Z[58])*Z[61];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M12()
{
  M[12][0] = -(Z[5]*Z[90]+Z[15]*Z[93])*Z[18];
  M[12][1] = (Z[29]*Z[99]-Z[15]*Z[96])*Z[31];
  M[12][2] = -(Z[102]*Z[32]+Z[105]*Z[15])*Z[45];
  M[12][3] = -(Z[54]*Z[111]+Z[59]*Z[114])*Z[61];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M17()
{
  M[17][0] = -(Z[139]*Z[9]+Z[64]*Z[14])*Z[18];
  M[17][1] = (Z[140]*Z[26]-Z[64]*Z[22])*Z[31];
  M[17][2] = -(Z[132]*Z[62]+Z[136]*Z[64])*Z[45];
  M[17][3] = -(Z[59]*Z[76]-Z[137]*Z[68])*Z[61];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M29()
{
  M[29][0] = -(Z[138]*Z[90]+Z[64]*Z[93])*Z[18];
  M[29][1] = (Z[141]*Z[99]-Z[64]*Z[96])*Z[31];
  M[29][2] = -(Z[147]*Z[63]+Z[149]*Z[64])*Z[45];
  M[29][3] = -(Z[59]*Z[123]-Z[137]*Z[117])*Z[61];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M34()
{
  M[34][0] = -(Z[77]*Z[153]+Z[79]*Z[157])*Z[18];
  M[34][1] = (Z[159]*Z[87]-Z[79]*Z[82])*Z[31];
  M[34][2] = -(Z[38]*Z[161]+Z[42]*Z[79])*Z[45];
  M[34][3] = -(Z[163]*Z[58]-Z[162]*Z[49])*Z[61];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M46()
{
  M[46][0] = -(Z[78]*Z[168]+Z[79]*Z[170])*Z[18];
  M[46][1] = (Z[158]*Z[128]-Z[79]*Z[125])*Z[31];
  M[46][2] = -(Z[102]*Z[160]+Z[105]*Z[79])*Z[45];
  M[46][3] = -(Z[163]*Z[114]-Z[162]*Z[108])*Z[61];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M51()
{
  M[51][0] = -(Z[142]*Z[153]+Z[144]*Z[157])*Z[18];
  M[51][1] = (Z[172]*Z[87]-Z[144]*Z[82])*Z[31];
  M[51][2] = -(Z[132]*Z[164]+Z[136]*Z[144])*Z[45];
  M[51][3] = -(Z[173]*Z[72]+Z[163]*Z[76])*Z[61];
}

void V2_4__d__u__em__ep__d__u__S5_0::Calculate_M63()
{
  M[63][0] = -(Z[143]*Z[168]+Z[144]*Z[170])*Z[18];
  M[63][1] = (Z[171]*Z[128]-Z[144]*Z[125])*Z[31];
  M[63][2] = -(Z[147]*Z[165]+Z[149]*Z[144])*Z[45];
  M[63][3] = -(Z[173]*Z[120]+Z[163]*Z[123])*Z[61];
}


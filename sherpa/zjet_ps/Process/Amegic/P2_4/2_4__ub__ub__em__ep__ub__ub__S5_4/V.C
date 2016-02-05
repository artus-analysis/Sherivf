#include "V.H"

using namespace AMEGIC;
using namespace ATOOLS;
using namespace std;

extern "C" Values* Getter_V2_4__ub__ub__em__ep__ub__ub__S5_4(Basic_Sfuncs* bs) {
  return new V2_4__ub__ub__em__ep__ub__ub__S5_4(bs);
}

V2_4__ub__ub__em__ep__ub__ub__S5_4::V2_4__ub__ub__em__ep__ub__ub__S5_4(Basic_Sfuncs* _BS) :
     Basic_Func(0,_BS),
     Basic_Zfunc(0,_BS),
     Basic_Pfunc(0,_BS)
{
  f = new int[4];
  c = new Complex[7];
  Z = new Complex[212];
  M = new Complex*[64];
  for(int i=0;i<64;i++) M[i] = new Complex[8];
  cl = new int[64];
}

V2_4__ub__ub__em__ep__ub__ub__S5_4::~V2_4__ub__ub__em__ep__ub__ub__S5_4()
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

Complex V2_4__ub__ub__em__ep__ub__ub__S5_4::Evaluate(int m,int n)
{
  if (cl[n]) return M[n][m];
  switch (n) {
    case 0: Calculate_M0(); break;
    case 12: Calculate_M12(); break;
    case 17: Calculate_M17(); break;
    case 18: Calculate_M18(); break;
    case 29: Calculate_M29(); break;
    case 30: Calculate_M30(); break;
    case 33: Calculate_M33(); break;
    case 34: Calculate_M34(); break;
    case 45: Calculate_M45(); break;
    case 46: Calculate_M46(); break;
    case 51: Calculate_M51(); break;
    case 63: Calculate_M63(); break;
  }
  cl[n]=1;
  return M[n][m];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M0()
{
  M[0][0] = (Z[8]*Z[1]+Z[13]*Z[9])*Z[18];
  M[0][1] = (Z[23]*Z[19]+Z[28]*Z[24])*Z[34];
  M[0][2] = -(Z[41]*Z[37]-Z[45]*Z[1])*Z[48];
  M[0][3] = (Z[52]*Z[1]+Z[57]*Z[53])*Z[61];
  M[0][4] = -(Z[52]*Z[62]+Z[57]*Z[63])*Z[66];
  M[0][5] = -(Z[28]*Z[67]+Z[23]*Z[68])*Z[69];
  M[0][6] = (Z[41]*Z[71]-Z[45]*Z[62])*Z[73];
  M[0][7] = -(Z[8]*Z[62]+Z[13]*Z[74])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M12()
{
  M[12][0] = (Z[111]*Z[1]+Z[114]*Z[14])*Z[18];
  M[12][1] = (Z[117]*Z[19]+Z[120]*Z[24])*Z[34];
  M[12][2] = -(Z[126]*Z[35]-Z[129]*Z[1])*Z[48];
  M[12][3] = (Z[132]*Z[1]+Z[135]*Z[58])*Z[61];
  M[12][4] = -(Z[132]*Z[62]+Z[135]*Z[64])*Z[66];
  M[12][5] = -(Z[120]*Z[67]+Z[117]*Z[68])*Z[69];
  M[12][6] = (Z[126]*Z[70]-Z[129]*Z[62])*Z[73];
  M[12][7] = -(Z[111]*Z[62]+Z[114]*Z[75])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M17()
{
  M[17][0] = (Z[152]*Z[77]+Z[157]*Z[79])*Z[18];
  M[17][1] = (Z[83]*Z[19]-Z[91]*Z[158])*Z[34];
  M[17][2] = -(Z[41]*Z[162]-Z[45]*Z[77])*Z[48];
  M[17][3] = (Z[52]*Z[77]+Z[57]*Z[163])*Z[61];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M18()
{
  M[18][4] = -(Z[52]*Z[106]+Z[57]*Z[165])*Z[66];
  M[18][5] = -(Z[28]*Z[167]-Z[32]*Z[158])*Z[69];
  M[18][6] = (Z[98]*Z[159]-Z[102]*Z[106])*Z[73];
  M[18][7] = -(Z[152]*Z[106]+Z[157]*Z[108])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M29()
{
  M[29][0] = (Z[175]*Z[77]+Z[178]*Z[78])*Z[18];
  M[29][1] = (Z[138]*Z[19]-Z[144]*Z[158])*Z[34];
  M[29][2] = -(Z[126]*Z[161]-Z[129]*Z[77])*Z[48];
  M[29][3] = (Z[132]*Z[77]+Z[135]*Z[164])*Z[61];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M30()
{
  M[30][4] = -(Z[132]*Z[106]+Z[135]*Z[166])*Z[66];
  M[30][5] = -(Z[120]*Z[167]-Z[123]*Z[158])*Z[69];
  M[30][6] = (Z[147]*Z[160]-Z[149]*Z[106])*Z[73];
  M[30][7] = -(Z[175]*Z[106]+Z[178]*Z[107])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M33()
{
  M[33][4] = -(Z[183]*Z[92]+Z[188]*Z[94])*Z[66];
  M[33][5] = -(Z[87]*Z[67]-Z[91]*Z[189])*Z[69];
  M[33][6] = (Z[41]*Z[191]-Z[45]*Z[92])*Z[73];
  M[33][7] = -(Z[8]*Z[92]+Z[13]*Z[192])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M34()
{
  M[34][0] = (Z[8]*Z[103]+Z[13]*Z[194])*Z[18];
  M[34][1] = (Z[23]*Z[196]-Z[32]*Z[189])*Z[34];
  M[34][2] = -(Z[98]*Z[179]-Z[102]*Z[103])*Z[48];
  M[34][3] = (Z[183]*Z[103]+Z[188]*Z[105])*Z[61];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M45()
{
  M[45][4] = -(Z[202]*Z[92]+Z[205]*Z[93])*Z[66];
  M[45][5] = -(Z[141]*Z[67]-Z[144]*Z[189])*Z[69];
  M[45][6] = (Z[126]*Z[190]-Z[129]*Z[92])*Z[73];
  M[45][7] = -(Z[111]*Z[92]+Z[114]*Z[193])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M46()
{
  M[46][0] = (Z[111]*Z[103]+Z[114]*Z[195])*Z[18];
  M[46][1] = (Z[117]*Z[196]-Z[123]*Z[189])*Z[34];
  M[46][2] = -(Z[147]*Z[180]-Z[149]*Z[103])*Z[48];
  M[46][3] = (Z[202]*Z[103]+Z[205]*Z[104])*Z[61];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M51()
{
  M[51][0] = (Z[152]*Z[168]+Z[157]*Z[198])*Z[18];
  M[51][1] = (Z[83]*Z[196]+Z[87]*Z[210])*Z[34];
  M[51][2] = -(Z[98]*Z[206]-Z[102]*Z[168])*Z[48];
  M[51][3] = (Z[183]*Z[168]+Z[188]*Z[170])*Z[61];
  M[51][4] = -(Z[183]*Z[171]+Z[188]*Z[173])*Z[66];
  M[51][5] = -(Z[87]*Z[167]+Z[83]*Z[211])*Z[69];
  M[51][6] = (Z[98]*Z[208]-Z[102]*Z[171])*Z[73];
  M[51][7] = -(Z[152]*Z[171]+Z[157]*Z[200])*Z[76];
}

void V2_4__ub__ub__em__ep__ub__ub__S5_4::Calculate_M63()
{
  M[63][0] = (Z[175]*Z[168]+Z[178]*Z[197])*Z[18];
  M[63][1] = (Z[138]*Z[196]+Z[141]*Z[210])*Z[34];
  M[63][2] = -(Z[147]*Z[207]-Z[149]*Z[168])*Z[48];
  M[63][3] = (Z[202]*Z[168]+Z[205]*Z[169])*Z[61];
  M[63][4] = -(Z[202]*Z[171]+Z[205]*Z[172])*Z[66];
  M[63][5] = -(Z[141]*Z[167]+Z[138]*Z[211])*Z[69];
  M[63][6] = (Z[147]*Z[209]-Z[149]*Z[171])*Z[73];
  M[63][7] = -(Z[175]*Z[171]+Z[178]*Z[199])*Z[76];
}


#ifndef DEFINES_ANALYZERS_H
#define DEFINES_ANALYZERS_H

// ROOT
#include "ROOT/RVec.hxx"
#include "TLorentzVector.h"

// EDM4hep
#include "edm4hep/MCParticleData.h"
#include "edm4hep/ReconstructedParticleData.h"

/**
 * @brief FCC analyzers collection.
 */
namespace FCCAnalyses {
using Vec_b = ROOT::VecOps::RVec<bool>;
using Vec_d = ROOT::VecOps::RVec<double>;
using Vec_f = ROOT::VecOps::RVec<float>;
using Vec_i = ROOT::VecOps::RVec<int>;
using Vec_ui = ROOT::VecOps::RVec<unsigned int>;

using rp = edm4hep::ReconstructedParticleData;
using Vec_rp = ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>;
using Vec_mc = ROOT::VecOps::RVec<edm4hep::MCParticleData>;
using Vec_tlv = ROOT::VecOps::RVec<TLorentzVector>;
} // namespace FCCAnalyses

#endif

import React, {useState} from "react"
import "./App.css"
import "h8k-components"

const medical_records = [
  {
    id: "1",
    data: [
      {
        id: 6,
        timestamp: 1568550058964,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 155,
          bloodPressureSystole: 90,
          pulse: 130,
          breathingRate: 29,
          bodyTemperature: 99.2
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 173
        }
      },
      {
        id: 7,
        timestamp: 1564691138999,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 147,
          bloodPressureSystole: 100,
          pulse: 138,
          breathingRate: 25,
          bodyTemperature: 100
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 196
        }
      },
      {
        id: 8,
        timestamp: 1562157191823,
        diagnosis: {
          id: 2,
          name: "Common Cold",
          severity: 1
        },
        vitals: {
          bloodPressureDiastole: 122,
          bloodPressureSystole: 77,
          pulse: 91,
          breathingRate: 20,
          bodyTemperature: 101.5
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 175
        }
      },
      {
        id: 13,
        timestamp: 1551906996274,
        diagnosis: {
          id: 2,
          name: "Common Cold",
          severity: 1
        },
        vitals: {
          bloodPressureDiastole: 121,
          bloodPressureSystole: 80,
          pulse: 91,
          breathingRate: 18,
          bodyTemperature: 101.3
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 180
        }
      },
      {
        id: 15,
        timestamp: 1551566179628,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 136,
          bloodPressureSystole: 88,
          pulse: 112,
          breathingRate: 25,
          bodyTemperature: 99.3
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 192
        }
      },
      {
        id: 22,
        timestamp: 1563243111785,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 139,
          bloodPressureSystole: 82,
          pulse: 105,
          breathingRate: 28,
          bodyTemperature: 97.1
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 196
        }
      },
      {
        id: 24,
        timestamp: 1563805161434,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 144,
          bloodPressureSystole: 92,
          pulse: 137,
          breathingRate: 34,
          bodyTemperature: 102.5
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 191
        }
      },
      {
        id: 30,
        timestamp: 1549051080085,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 130,
          bloodPressureSystole: 82,
          pulse: 114,
          breathingRate: 23,
          bodyTemperature: 98.6
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 188
        }
      },
      {
        id: 33,
        timestamp: 1552027463340,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 133,
          bloodPressureSystole: 83,
          pulse: 126,
          breathingRate: 19,
          bodyTemperature: 99.7
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 185
        }
      },
      {
        id: 41,
        timestamp: 1546789224456,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 151,
          bloodPressureSystole: 96,
          pulse: 130,
          breathingRate: 26,
          bodyTemperature: 103
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 1,
        userName: "John Oliver",
        userDob: "02-01-1986",
        meta: {
          height: 168,
          weight: 174
        }
      }
    ]
  },
  {
    id: "2",
    data: [
      {
        id: 1,
        timestamp: 1565637002408,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 154,
          bloodPressureSystole: 91,
          pulse: 125,
          breathingRate: 32,
          bodyTemperature: 100
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 172
        }
      },
      {
        id: 2,
        timestamp: 1562539731129,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 139,
          bloodPressureSystole: 81,
          pulse: 104,
          breathingRate: 20,
          bodyTemperature: 99.4
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 171
        }
      },
      {
        id: 3,
        timestamp: 1563465027370,
        diagnosis: {
          id: 2,
          name: "Common Cold",
          severity: 1
        },
        vitals: {
          bloodPressureDiastole: 125,
          bloodPressureSystole: 76,
          pulse: 113,
          breathingRate: 22,
          bodyTemperature: 100.8
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 185
        }
      },
      {
        id: 16,
        timestamp: 1568085122164,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 136,
          bloodPressureSystole: 85,
          pulse: 117,
          breathingRate: 29,
          bodyTemperature: 99.9
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 186
        }
      },
      {
        id: 17,
        timestamp: 1547084560364,
        diagnosis: {
          id: 2,
          name: "Common Cold",
          severity: 1
        },
        vitals: {
          bloodPressureDiastole: 129,
          bloodPressureSystole: 79,
          pulse: 102,
          breathingRate: 16,
          bodyTemperature: 103.4
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 185
        }
      },
      {
        id: 20,
        timestamp: 1549184918171,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 145,
          bloodPressureSystole: 94,
          pulse: 125,
          breathingRate: 25,
          bodyTemperature: 102.6
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 181
        }
      },
      {
        id: 26,
        timestamp: 1564765981840,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 144,
          bloodPressureSystole: 90,
          pulse: 135,
          breathingRate: 28,
          bodyTemperature: 99.2
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 178
        }
      },
      {
        id: 31,
        timestamp: 1555004832077,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 154,
          bloodPressureSystole: 90,
          pulse: 138,
          breathingRate: 26,
          bodyTemperature: 102.9
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 178
        }
      },
      {
        id: 32,
        timestamp: 1554074088481,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 135,
          bloodPressureSystole: 82,
          pulse: 119,
          breathingRate: 29,
          bodyTemperature: 97.8
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 183
        }
      },
      {
        id: 35,
        timestamp: 1560628606015,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 151,
          bloodPressureSystole: 98,
          pulse: 140,
          breathingRate: 27,
          bodyTemperature: 100.7
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 2,
        userName: "Bob Martin",
        userDob: "14-09-1989",
        meta: {
          height: 174,
          weight: 186
        }
      }
    ]
  },
  {
    id: "3",
    data: [
      {
        id: 9,
        timestamp: 1548036340751,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 147,
          bloodPressureSystole: 96,
          pulse: 130,
          breathingRate: 28,
          bodyTemperature: 101
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 106
        }
      },
      {
        id: 10,
        timestamp: 1562161672195,
        diagnosis: {
          id: 2,
          name: "Common Cold",
          severity: 1
        },
        vitals: {
          bloodPressureDiastole: 127,
          bloodPressureSystole: 78,
          pulse: 130,
          breathingRate: 22,
          bodyTemperature: 103.8
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 110
        }
      },
      {
        id: 11,
        timestamp: 1563846626267,
        diagnosis: {
          id: 2,
          name: "Common Cold",
          severity: 1
        },
        vitals: {
          bloodPressureDiastole: 126,
          bloodPressureSystole: 75,
          pulse: 99,
          breathingRate: 22,
          bodyTemperature: 101.9
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 108
        }
      },
      {
        id: 18,
        timestamp: 1560177927736,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 141,
          bloodPressureSystole: 96,
          pulse: 123,
          breathingRate: 29,
          bodyTemperature: 99
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 103
        }
      },
      {
        id: 25,
        timestamp: 1551539005307,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 154,
          bloodPressureSystole: 90,
          pulse: 131,
          breathingRate: 22,
          bodyTemperature: 103
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 107
        }
      },
      {
        id: 27,
        timestamp: 1556836728887,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 133,
          bloodPressureSystole: 84,
          pulse: 124,
          breathingRate: 26,
          bodyTemperature: 99.2
        },
        doctor: {
          id: 2,
          name: "Dr Arnold Bullock"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 109
        }
      },
      {
        id: 29,
        timestamp: 1551436887626,
        diagnosis: {
          id: 2,
          name: "Common Cold",
          severity: 1
        },
        vitals: {
          bloodPressureDiastole: 124,
          bloodPressureSystole: 80,
          pulse: 129,
          breathingRate: 21,
          bodyTemperature: 102.3
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 107
        }
      },
      {
        id: 34,
        timestamp: 1553964012428,
        diagnosis: {
          id: 3,
          name: "Pulmonary embolism",
          severity: 4
        },
        vitals: {
          bloodPressureDiastole: 151,
          bloodPressureSystole: 95,
          pulse: 126,
          breathingRate: 29,
          bodyTemperature: 102.9
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 102
        }
      },
      {
        id: 42,
        timestamp: 1551568255913,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 133,
          bloodPressureSystole: 86,
          pulse: 115,
          breathingRate: 26,
          bodyTemperature: 97.7
        },
        doctor: {
          id: 3,
          name: "Dr Pilar Cristancho"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 110
        }
      },
      {
        id: 47,
        timestamp: 1568317109556,
        diagnosis: {
          id: 4,
          name: "Pleurisy",
          severity: 3
        },
        vitals: {
          bloodPressureDiastole: 139,
          bloodPressureSystole: 83,
          pulse: 124,
          breathingRate: 26,
          bodyTemperature: 99.7
        },
        doctor: {
          id: 4,
          name: "Dr Allysa Ellis"
        },
        userId: 3,
        userName: "Helena Fernandez",
        userDob: "23-12-1987",
        meta: {
          height: 157,
          weight: 104
        }
      }
    ]
  }
]
const title = "Patient Medical Records"

function Records({record, onNext}) {
  if (!record) return null

  return (
    <div className="patient-profile-container" id="profile-view">
      <div className="layout-row justify-content-center">
        <div id="patient-profile" data-testid="patient-profile" className="mx-auto">
          <h4 id="patient-name">{record.data[0].userName}</h4>
          <h5 id="patient-dob">DOB: {record.data[0].userDob}</h5>
          <h5 id="patient-height">Height: {record.data[0].meta.height} cm</h5>
        </div>
        <button
          className="mt-10 mr-10"
          data-testid="next-btn"
          onClick={onNext}
        >
          Next
        </button>
      </div>

      <table id="patient-records-table">
        <thead id="table-header">
        <tr>
          <th>SL</th>
          <th>Date</th>
          <th>Diagnosis</th>
          <th>Weight</th>
          <th>Doctor</th>
        </tr>
        </thead>
        <tbody id="table-body" data-testid="patient-table">
        {record.data.map((r, idx) => (
          <tr key={r.id}>
            <td>{idx + 1}</td>
            <td>{new Date(r.timestamp).toLocaleDateString("en-GB")}</td>
            <td>{r.diagnosis.name}</td>
            <td>{r.meta.weight}</td>
            <td>{r.doctor.name}</td>
          </tr>
        ))}
        </tbody>
      </table>
    </div>
  )
}

function Search({onShow}) {
  const [selected, setSelected] = useState("")

  return (
    <div className="layout-row align-items-baseline select-form-container">
      <div className="select">
        <select
          data-testid="patient-name"
          value={selected}
          onChange={(e) => setSelected(e.target.value)}
        >
          <option value="" disabled>
            Select Patient
          </option>
          {medical_records.map((p) => (
            <option key={p.id} value={p.id}>
              {p.data[0].userName}
            </option>
          ))}
        </select>
      </div>

      <button
        type="button"
        data-testid="show"
        onClick={() => onShow(selected)}
      >
        Show
      </button>
    </div>
  )
}


const App = () => {
  const [currentRecord, setCurrentRecord] = useState(null)

  const handleShow = (id) => {
    if (!id) {
      alert("Please select a patient name")
      return
    }
    const patient = medical_records.find((p) => p.id === id)
    setCurrentRecord(patient)
  }

  const handleNext = () => {
    if (!currentRecord) return
    const currentIndex = medical_records.findIndex((p) => p.id === currentRecord.id)
    const nextIndex = (currentIndex + 1) % medical_records.length
    setCurrentRecord(medical_records[nextIndex])
  }

  return (
    <div className="App">
      <h8k-navbar header={title}></h8k-navbar>
      <div className="content">
        <Search onShow={handleShow}/>
        <Records record={currentRecord} onNext={handleNext}/>
      </div>
    </div>
  )
}

export default App

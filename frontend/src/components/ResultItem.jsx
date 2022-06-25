import React from "react";
import { AiOutlineInfoCircle } from "react-icons/ai";
function ResultItem(result) {
  console.log(result);
  return (
    <div className="card shadow-md compact side bg-base-100">
      <div className="flex-row items-center space-x-4 card-body">
        <div>
          <div className="avatar">
            <div className="rounded-full shadow h-14 w-14">
              <AiOutlineInfoCircle className="w-10 h-10" />
            </div>
          </div>
        </div>

        <div>
          <h2 className="card-title">{result.text}</h2>
        </div>
      </div>
    </div>
  );
}

export default ResultItem;

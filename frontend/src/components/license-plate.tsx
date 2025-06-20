import React from "react";

interface CarPlateProps {
  plate: string;
}

const LicensePlate: React.FC<CarPlateProps> = ({ plate }) => {
  const match = /^([А-ЯA-Z])(\d{3})([А-ЯA-Z]{2})(\d{2,3})$/.exec(
    plate.replace(/\s+/g, ""),
  );

  if (!match) {
    return (
      <div className="border-border w-fit rounded-sm border-2 px-3 text-3xl font-medium">
        {plate}
      </div>
    );
  }

  const [, letter1, digits, letters2, region] = match;

  return (
    <div className="border-border flex w-fit overflow-hidden rounded-sm border-2">
      <div className="flex items-end gap-0.5 px-2 text-2xl font-semibold uppercase">
        <span>{letter1}</span>
        <span className="text-3xl">{digits}</span>
        <span>{letters2}</span>
      </div>

      <div className="flex flex-col border-l-2 px-1">
        <span className="text-xl leading-5 font-semibold">{region}</span>
        <span className="text-xs leading-3 font-medium">RUS</span>
      </div>
    </div>
  );
};

export default LicensePlate;
